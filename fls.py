from flask import Flask, send_file, request, render_template, jsonify, make_response, url_for
import json
from functools import wraps, partial
from hexagram import Hexagram, Trigram
app = Flask(__name__)
with app.app_context():
    app.config["SERVER_NAME"] = "cleromancer.herokuapp.com"

def link_dict(func, ep, *args, **kwargs):
    ls = []
    with app.app_context():
        for idx, arg in enumerate(['first', 'last', 'next']):
            # kwargs only contains a single item, so this is horrible
            for k, v in kwargs.items():
                kwargs[k] = args[idx]
            url = func(ep, **kwargs)
            ls.append('<%s>; rel="%s"' % (url, arg))
    return ','.join(ls)

def add_response_headers(headers={}):
    """This decorator adds the headers passed in to the response"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in headers.items():
                h[header] = value
            return resp
        return decorated_function
    return decorator

def link_next():
    links = {}
    kwargs = {}
    ep = request.endpoint
    # if it's a hexagram call
    if request.view_args.get('hexagram'):
        first = '000000'
        last = '11111'
        kwargs['hexagram'] = 'dummy'
        num = request.view_args.get('hexagram')
        # reverse input, and convert to int
        rev = int(num[::-1], 2)
        if rev >= 63:
            _next = first
        else:
            rev += 1
            # reverse again, and pad
            _next = bin(rev)[2:].zfill(6)[::-1]
    # must be a trigram call
    else:
        first = '000'
        last = '111'
        kwargs['trigram'] = 'dummy'
        num = request.view_args.get('trigram')
        # reverse input, and convert to int
        rev = int(num[::-1], 2)
        if rev >= 7:
            _next = first
        else:
            rev += 1
            # reverse again, and pad
            _next = bin(rev)[2:].zfill(3)[::-1]
    # first, next, previous, last
    links["Link"] = '%s' % (
        link_dict(url_for, ep, first, last, _next, **kwargs),
    )
    return links

@app.route('/hexagram/<hexagram>.png')
def hex_out(hexagram):
    generated = Hexagram([int(elem) for elem in hexagram])
    response = make_response(send_file(generated.dump_image(), mimetype='image/png'))
    for k, v in link_next().items():
        response.headers[k] = v
    return response

@app.route('/trigram/<trigram>.png')
def tri_out(trigram):
    generated = Trigram([int(elem) for elem in trigram])
    response = make_response(send_file(generated.dump_image(), mimetype='image/png'))
    for k, v in link_next().items():
        response.headers[k] = v
    return response

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

def link_first():
    with app.app_context():
        return {"Link": '<%s>; rel="first"' % url_for(
            'hex_out',
            hexagram='000000',
            _external=True)
        }

def firstlink(f):
    """ Return the link to the simplest hexagram with a response """
    @wraps(f)
    @add_response_headers(link_first())
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@firstlink
def index():
    msg = {
        "Hexagram": "/hexagram/nnnnnn.png, where n is 1 (solid bar) or 0 (broken bar). Hexagrams are built bottom to top.",
        "Trigram": "/trigram/nnn.png, where n is 1 (solid bar) or 0 (broken bar). Trigrams are built bottom to top."
    }
    if request_wants_json():
        return jsonify(items=[json.dumps(msg)])
    return render_template('index.html'), 200

@app.errorhandler(404)
def page_not_found(error):
    error = {
        "Hexagram": "/hexagram/nnnnnn.png, where n is 1 (solid bar) or 0 (broken bar). Hexagrams are built bottom to top.",
        "Trigram": "/trigram/nnn.png, where n is 1 (solid bar) or 0 (broken bar). Trigrams are built bottom to top."
    }
    if request_wants_json():
        resp = make_response(jsonify(items=[json.dumps(error)]), 404)
    resp = make_response(render_template('index.html'), 404)
    return resp

@app.errorhandler(500)
def app_error(error):
    error = {
        "Hexagram": "/hexagram/nnnnnn.png, where n is 1 (solid bar) or 0 (broken bar). Hexagrams are built bottom to top.",
        "Trigram": "/trigram/nnn.png, where n is 1 (solid bar) or 0 (broken bar). Trigrams are built bottom to top."
    }
    if request_wants_json():
        return jsonify(items=[json.dumps(error)]), 500
    return render_template('index.html'), 500

if __name__ == '__main__':
    app.run()

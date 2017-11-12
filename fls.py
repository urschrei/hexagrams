# -*- coding: utf-8 -*-

import os
from flask import Flask, send_file, request, render_template, jsonify, make_response, url_for
from functools import wraps
from hexagram import Hexagram, Trigram
app = Flask(__name__)
with app.app_context():
    app.config["SERVER_NAME"] = os.environ.get("SERVER_NAME")

def json_resp():
    return {
        "hexagram": "/hexagram/nnnnnn.png, where n is 1 (solid bar) or 0 (broken bar). Hexagrams are built bottom to top.",
        "trigram": "/trigram/nnn.png, where n is 1 (solid bar) or 0 (broken bar). Trigrams are built bottom to top.",
        "digit_order": "Hexagrams and Trigrams are built using digits read from left to right.",
        "links": "See the Link header for full paths.",
        "copyright": "Stephan Hügel, 2016"
    }

def link_dict(func, ep, *args, **kwargs):
    """ Build "Link" headers from a list of passed values
    kwargs only contains one key: it's passed to the url builder func
    we replace its value with the first, last, and next values, then build
    the url, and append as string
    """
    links = []
    with app.app_context():
        for idx, arg in enumerate(['first', 'last', 'next']):
            # kwargs only contains a single key (hexagram or trigram)
            # its value is replaced by the first, next, and last digit sequences
            # args contains values for first, last next
            for k in kwargs.keys():
                kwargs[k] = args[idx]
            kwargs['_external'] = True
            url = func(ep, **kwargs)
            links.append('<%s>; rel="%s"' % (url, arg))
    return ', '.join(links)

def add_response_headers(headers={}):
    """ This decorator adds the headers passed in to the response"""
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

def step_calculation(num, _max):
    """ Calculate next hexagram or trigram binary representation
    Overflows to smallest
    """
    if _max == 63:
        first = '000000'
        zf = 6
    else:
        first = '000'
        zf = 3
    # reverse input, and convert to int
    rev = int(num[::-1], 2)
    if rev >= max:
        out = first
    else:
        rev += 1
        # reverse again, and pad
        out = bin(rev)[2:].zfill(zf)[::-1]
    return out

def link_next():
    links = {}
    kwargs = {}
    # if it's a hexagram call
    if request.view_args.get('hexagram'):
        first = '000000'
        last = '11111'
        kwargs['hexagram'] = 'dummy'
        num = request.view_args.get('hexagram')
        _next = step_calculation(num, 63)
    # must be a trigram call
    else:
        first = '000'
        last = '111'
        kwargs['trigram'] = 'dummy'
        num = request.view_args.get('trigram')
        _next = step_calculation(num, 7)
    # first, next, previous, last
    links["Link"] = '%s' % (
        link_dict(url_for, request.endpoint, first, last, _next, **kwargs),
    )
    return links

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

@app.route('/')
@firstlink
def index():
    if request_wants_json():
        msg  = json_resp()
        return jsonify(items=[msg])
    return render_template('index.html'), 200

@app.errorhandler(404)
def page_not_found(error):
    if request_wants_json():
        return  make_response(jsonify(items=["Not Found"]), 404)
    return make_response(render_template('index.html'), 404)

@app.errorhandler(500)
def app_error(error):
    if request_wants_json():
        return jsonify(items=["Internal Server Error"]), 500
    return render_template('index.html'), 500

if __name__ == '__main__':
    app.run()

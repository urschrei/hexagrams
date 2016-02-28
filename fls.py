from flask import Flask, send_file, request, render_template, jsonify, make_response, url_for
import json
from functools import wraps
from hexagram import Hexagram, Trigram
app = Flask(__name__)

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

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

def firstlink(f):
    """ Return the link to the simplest hexagram with a response """
    @wraps(f)
    @add_response_headers({"Link": '<%s>; rel="first"' % url_for(
        "hex_out",
        hexagram='000000',
        _external=True)}
    )
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

@app.route('/hexagram/<hexagram>.png')
def hex_out(hexagram):
    generated = Hexagram([int(elem) for elem in hexagram])
    return send_file(generated.dump_image(), mimetype='image/png')

@app.route('/trigram/<trigram>.png')
def tri_out(trigram):
    generated = Trigram([int(elem) for elem in trigram])
    return send_file(generated.dump_image(), mimetype='image/png')

@app.errorhandler(404)
def page_not_found(error):
    error = {
        "Hexagram": "/hexagram/nnnnnn.png, where n is 1 (solid bar) or 0 (broken bar). Hexagrams are built bottom to top.",
        "Trigram": "/trigram/nnn.png, where n is 1 (solid bar) or 0 (broken bar). Trigrams are built bottom to top."
    }
    if request_wants_json():
        return jsonify(items=[json.dumps(error)])
    return render_template('index.html'), 404

@app.errorhandler(500)
def app_error(error):
    error = {
        "Hexagram": "/hexagram/nnnnnn.png, where n is 1 (solid bar) or 0 (broken bar). Hexagrams are built bottom to top.",
        "Trigram": "/trigram/nnn.png, where n is 1 (solid bar) or 0 (broken bar). Trigrams are built bottom to top."
    }
    if request_wants_json():
        return jsonify(items=[json.dumps(error)])
    return render_template('index.html'), 500

if __name__ == '__main__':
    app.run()

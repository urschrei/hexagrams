from flask import Flask, send_file
app = Flask(__name__)
from hexagram import Hexagram, Trigram

@app.route('/hexagram/<hexagram>.png')
def hex_out(hexagram):
    generated = Hexagram([int(elem) for elem in hexagram])
    return send_file(generated.dump_image(), mimetype='image/png')

@app.route('/trigram/<trigram>.png')
def tri_out(trigram):
    generated = Trigram([int(elem) for elem in trigram])
    return send_file(generated.dump_image(), mimetype='image/png')

if __name__ == '__main__':
    app.run()

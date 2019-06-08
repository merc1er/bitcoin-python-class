from flask import Flask, render_template
from bitcash import Key


app = Flask(__name__)

HOST = '0.0.0.0'
DEBUG = True
PORT = 5000

EVENT_BRIBE_LINK = '#'


@app.route('/')
def index():
    key = Key()
    wif = key.to_wif()
    return render_template(
        'index.html',
        eb_link=EVENT_BRIBE_LINK,
        address=key.address,
        wif=wif,
    )


if __name__ == '__main__':
    app.run(host=HOST, debug=DEBUG, port=PORT)

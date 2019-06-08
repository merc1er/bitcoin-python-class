from flask import Flask, render_template, session
from bitcash import Key
import secrets


app = Flask(__name__)
app.secret_key = 'c4038aaabec76362aa9f104d089936471144c97d62'

HOST = '0.0.0.0'
DEBUG = True
PORT = 5000

EVENT_BRIBE_LINK = '#'


@app.route('/')
def index():
    if 'user' not in session:
        session['user'] = secrets.token_hex()
        key = Key()
        wif = key.to_wif()
        # Stores the keys in the cookies
        session['wif'] = wif
        session['address'] = key.address

    return render_template(
        'index.html',
        eb_link=EVENT_BRIBE_LINK,
        address=session['address'],
        wif=session['wif'],
    )


if __name__ == '__main__':
    app.run(host=HOST, debug=DEBUG, port=PORT)

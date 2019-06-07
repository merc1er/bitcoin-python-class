from flask import Flask, render_template


app = Flask(__name__)

HOST = '0.0.0.0'
DEBUG = True
PORT = 5000

EVENT_BRIBE_LINK = '#'


@app.route('/')
def index():
    return render_template('index.html', eb_link=EVENT_BRIBE_LINK)


if __name__ == '__main__':
    app.run(host=HOST, debug=DEBUG, port=PORT)

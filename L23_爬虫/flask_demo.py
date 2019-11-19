from flask import Flask
import time

app = Flask(__name__)


@app.route('/tiger')
def index_tiger():
    time.sleep(2)
    return 'Hello tiger'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello jay'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello tom'


if __name__ == '__main__':
    app.run(threaded=True)

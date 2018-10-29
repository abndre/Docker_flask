from flask import Flask, request
from flask import jsonify
import udptest

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/udptest')
def udpt():
    test = udptest.testudp()
    test = jsonify(test)
    return test

@app.route('/udp/', methods=['GET'])
def udpproduction():
    # e.g: http://localhost:5000/udp/?url=www.google.com&cont=4
    bar = request.args.to_dict()
    url = bar['url']
    cont = bar['cont']
    test = udptest.testudp()
    test = jsonify(test)
    '''
    return e.g.
    {
    "avg": 10.774,
    "max": 11.802,
    "min": 9.22
    }
    '''
    return test


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

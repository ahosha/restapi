from flask import Flask
from flask import request
import redis
import json


app = Flask(__name__)


@app.route('/setredis/', methods=['POST'])
# http://127.0.0.1:5000/setredis?key=keyfrompython1&value=vlauefrompostman
def setredis():
    key = request.args.get('key')
    value = request.args.get('value')
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set(key, value)
    return "set done!"


@app.route('/getredis', methods=['GET'])
# http://127.0.0.1:5000/getredis?key=keyfrompython1
# @app.route('/getredis/<string:key>/', methods=['GET'])
# http://127.0.0.1:5000/getredis/keyfrompython
# def getredis(key):
def getredis():
    key = request.args.get('key')
    r = redis.Redis(host='localhost', port=6379, db=0)
    try:
        value = r.get(key)
        if value:
            return value
        else:
            return 'no data for this key'
    except:
        return None

@app.route('/getallkeys', methods=['GET'])
# http://127.0.0.1:5000/getallkeys
def getallkeys():
    r = redis.Redis(host='localhost', port=6379, db=0)
    retlist = [];
    for key in r.scan_iter():
        retlist.append(key.decode("utf-8"))
    print(retlist)
    return json.dumps(retlist)



if __name__ == '__main__':
    app.run()

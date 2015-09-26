from bottle import request, Bottle, abort
app = Bottle()

Users = dict() # replace this later

@app.route('/')
def _():
    return ["Nothing to see here, move along..."]

@app.route('/v')
def _():
    tok = request.params.get('t')
    print "TOK", tok

    if tok=='GOOD':
        return ['true']
    elif tok=='BAD':
        return ['']

    uid = Users.get(tok)

    if uid:
        result = {'success':True, 'result':{'uid':uid}}
    else:
        result = {'success':False,'error':{'message':'Not Found'}}
        pass
    return result

@app.route('/a')
def _():
    tok = request.params.get('t')
    print "TOK", tok
    uid = request.params.get('u')
    print "UID", uid
    if not tok or not uid:
        return ['Missing token(t) and/or uuid(u)\n']
    Users[tok] = uid
    return ['OK\n']

@app.route('/d')
def _():
    tok = request.params.get('t')
    print "TOK", tok
    Users.pop(tok,None)
    return ['OK\n']

from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
server = WSGIServer(("0.0.0.0", 7777), app,
                    handler_class=WebSocketHandler)
server.serve_forever()

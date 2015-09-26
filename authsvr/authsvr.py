#!/usr/bin/env python
from gevent import monkey; monkey.patch_all()
import os, sys, traceback as tb, sqlite3
from bottle import request, Bottle, abort
from misc import add_cors_headers
from uuid import uuid1, uuid4

app = Bottle()

Users = dict() # in-memory cache
_conn = None   # storage for DB()

def DB():
    print "DB"
    global _conn
    if not _conn:
        _conn = sqlite3.connect('auth.db')
        _conn.execute('''CREATE TABLE IF NOT EXISTS tokens (tok text, uid text)''')
        rs = _conn.execute('''SELECT tok,uid FROM tokens''')
        for row in rs:
            tok,uid = row
            print "Load tok=%s,uid=%s" % (tok,uid)
            Users[tok] = uid
            pass
        pass
    return _conn

DB()

@app.route('/')
def _():
    return ["Nothing to see here, move along..."]

@app.route('/v')
def _():
    add_cors_headers()

    tok = request.params.get('t')
    print "TOK", tok

    uid = Users.get(tok)
    if uid:
        result = {'success':True, 'result':{'uid':uid}}
    else:
        result = {'success':False,'error':{'message':'Not Found'}}
        pass
    return result

@app.route('/a')
def _():
    add_cors_headers()

    tok = str(uuid1())
    print "TOK", tok
    uid = request.params.get('u')
    print "UID", uid
    if not tok or not uid:
        return ['Missing uuid(u)\n']
    Users[tok] = uid
    DB().execute('INSERT INTO tokens (tok,uid) VALUES (?,?)', (tok, uid))
    DB().commit()
    return {'success':True, 'result':{'uid':uid,'token':tok}}

@app.route('/d')
def _():
    tok = request.params.get('t')
    print "TOK", tok
    Users.pop(tok,None)
    DB().execute('DELETE FROM tokens WHERE tok=?', (tok, ))
    DB().commit()
    return ['OK\n']

from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
server = WSGIServer(("0.0.0.0", 7777), app,
                    handler_class=WebSocketHandler)
server.serve_forever()

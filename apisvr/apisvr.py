#!/usr/bin/env python
"""
serve up the kno api

"""
from gevent import monkey
monkey.patch_all()
from bottle import route, run, template, request, response, static_file, default_app, redirect
import requests, json, os, sys, gevent, traceback
from requests.auth import HTTPBasicAuth
from thekno.misc import add_cors_headers

LOG = open('/tmp/kno.LOG','a+',0)

# https://alchemyapi.readme.io/v1.0/docs/rest-api-documentation

#ApiKey = '562d48f76a5e059e16c8422b5df77c8e57da9f19' # jmward@gmail.com
ApiKey = '85e62ad889b1b15314bb96cf6387592215231fc5'

ApiKey = '1d229f72ad6b7027408bd5957cb8b31df6a812a5'

MaxResults = 2
Pfx = 'https://gateway-a.watsonplatform.net'

def saveit(outfile,text):
    """
    save the wav!
    """
    print >>LOG, "SAVEIT", outfile

    if os.path.isfile('static/wav/' + outfile + '.wav'):
        print >>LOG, "Ok it already exists", outfile
        return

    try:
        f = open('static/wav/%s.txt' % outfile,'w')
        print >>f, text
        f.close()
        ret = _saveit2(outfile,text)
        print >>LOG, "SAVEDIT", outfile
        return ret
    except:
        print >>LOG, '*'*80
        print >>LOG, traceback.format_exc()[:100]
        print >>LOG, '*'*80
        pass

def _saveit2(outfile,text):
    text = text.replace('"','')
    url = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"
    username='474bf77c-0e50-4aca-a1ce-b3100f217aec'
    password='Nql0dzKQToEv'
    resp = requests.get(url, params=dict(text=text,
                                         voice='en-GB_KateVoice',
                                     ), auth=HTTPBasicAuth(username, password))

    filename = 'static/wav/' + outfile + '.wav'
    chunk_size = 1024
    with open(filename, 'wb') as fd:
        for chunk in resp.iter_content(chunk_size):
            fd.write(chunk)

    print >>LOG, "FINISHED WRITE", outfile

    cmd = "ffmpeg -i static/wav/%s.wav static/wav/%s.mp3" % ( outfile, outfile, )
    print >>LOG, cmd
    os.system( cmd )
    pass

@route('/static/<filename:path>')
def send_static(filename):
    """
    serve up files in the static directory.
    Dev Only!
    """
    print "SEND STATIC", filename
    print >>LOG, "STATIC"
    return static_file(filename, root='./static/')

@route('/xtnsLeftToday')
def xtnsLeftToday():
    """
    how many transactions left today?
    """
    print "XTNS LEFT TODAY"
    print >>LOG, "XTNS LEFT"
    add_cors_headers()
    
    import xmltodict
    url = 'http://access.alchemyapi.com/calls/info/GetAPIKeyInfo?apikey=' + ApiKey
    r = requests.get(url, verify=False)
    text = r.text
    x = xmltodict.parse(text)
    print x
    ret = json.dumps(x)
    print ret
    print >>LOG, "XTNS DONE"
    return [ret]

@route('/top')
def top():
    """
    /top?term=<EntityTerm>[&max=<MaxEntries>]

    top news articles
    """
    print "TOP"
    print >>LOG, "START TOP"
    try:
        return _2()
    except:
        print >>LOG, '*'*80
        print >>LOG, traceback.format_exc()
        print >>LOG, '*'*80
        pass

def _2():
    response.headers['Access-Control-Allow-Origin'] = '*'
    max_results = request.params.get('max',MaxResults)
    term = request.params.get('term','Bernie+Sanders')

    print >>LOG, "/top request for %s" % term
    term = term.replace('%20','+')

    cached = False

    try:
        with open('history/term:%s.json' % term) as fd:
            text = fd.read()
            print >>LOG, "do it old"
            cached = True
            #return [ text ]
    except:
        print >>LOG, "do it fresh"

        count = 5

        returnVar = ','.join(['enriched.url.url',
                     'enriched.url.image',
                     'enriched.url.title',
                     'enriched.url.text',
                     'enriched.url.entities'])

        rangeStart = 'now-10d'
        rangeEnd = 'now'


        url = (Pfx + '/calls/data/GetNews?' +
               'outputMode=json&' +
               'start=%s&' +
               'end=%s&'+
               'count=%s&'+
               'q.enriched.url.enrichedTitle.entities.entity=|text=%s|&'+
               'maxResults=%s&' +
               'return=%s&'+
               'apikey=%s') % (rangeStart,rangeEnd,count,term,max_results,returnVar,ApiKey,)
        r = requests.get(url, verify=False)
        text = r.text
        pass

    print >>LOG, "remote req complete"
    j = json.loads( text )
    print >>LOG, "remote req complete2: result: ", json.dumps(j)[:100]

    if j['status'] == 'ERROR':
        print >>LOG, "remote req ERROR: ", json.dumps(j)[:100]
        return j

    if not cached:
        with open('history/term:%s.json' % term, 'wb') as fd:
            fd.write( text )
            pass
        pass

    print "TEXT", text

    result = j["result"]

    if 'docs' not in result:
        return ['[]']

    lst = result["docs"]

    arr = []
    print >>LOG, "remote req really complete", [ x['id'] for x in lst]
    for x in lst:
        print >>LOG, "X", x['id']
        id = x['id']
        rec = x["source"]["enriched"]["url"]
        title = unicode(rec["title"])
        title = title.encode('ascii','ignore')
        text  = unicode(rec["text"])
        text = text.encode('ascii','ignore')

        #title = rec["title"]
        #text  = rec["text"]

        text = text.replace("'", "")
        text = text.replace("\"", "")
        text = text.replace("<", "")
        text = text.replace(">", "")
        text = text.replace("\\", "")
        text = text.replace("\r", "")
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")

        print >>LOG, "1X1", x['id']
        prefetch_audio = request.params.get('prefetch')
        print >>LOG, "1Xg", prefetch_audio
        if prefetch_audio:
            print >>LOG, "1X2", x['id']
            gevent.spawn( saveit, id, text )
            print >>LOG, "1X3", x['id']
            print >>LOG, "1X2", x['id']
            gevent.spawn( saveit, id+'_title', title )
            print >>LOG, "1X3", x['id']
            pass

        entities = rec["entities"]
        earr = []
        for e in entities:
            earr.append( e['text'] )
            pass
        
        #url2  = unicode(rec["url"])
        #image = unicode(rec["image"])
        url2  = rec["url"]
        image = rec.get("image")

        if 'tumblr' in url2:
            continue

        arr.append( dict( id=id, title=title, url=url2, entities=earr,
                          text=text, image=image) )
        pass
    r2 = json.dumps( arr, indent = 5 )
    print >>LOG, "X9", x['id']
    return [r2]

'''
@route('/news')
def _():
    ret = []
    max_results = request.params.get('xxx',MaxResults)
    print max_results
    url = "https://gateway-a.watsonplatform.net/calls/data/GetNews?apikey=%s&outputMode=json&start=now-1d&end=now&maxResults=%s&q.enriched.url.enrichedTitle.relations.relation=|action.verb.text=acquire,object.entities.entity.type=Company|&return=enriched.url.title" % (ApiKey,max_results)
    resp = requests.get(url, verify=False)
    print resp
    j = resp.json()
    print j
    print json.dumps(j)
    j2 = json.dumps(j, indent=5)
    print j2
    return [ j2 ]
'''

@route('/')
def index():
    """
    return ["BLAH"]
    """
    print "INDEX"
    return ["BLAH"]

@route('/debug')
def debug():
    """
    redirect('/static/index.html')
    """
    redirect('/static/index.html')

from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler

if __name__=='__main__':
    print "MAINx"
    print >>LOG, "== RESTART =="
    server = WSGIServer(("0.0.0.0", 6001), default_app(),
                        handler_class=WebSocketHandler)
    server.serve_forever()

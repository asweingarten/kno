Help on module apisvr:

NAME
    apisvr - serve up the kno api

FILE
    /Users/val/src/kno/apisvr/apisvr.py

FUNCTIONS
    debug()
        redirect('/static/index.html')
    
    index()
        return ["BLAH"]
    
    saveit(outfile, text)
        save the wav!
    
    send_static(filename)
        serve up files in the static directory.
        Dev Only!
    
    top()
        /top?term=<EntityTerm>[&max=<MaxEntries>]
        
        top news articles
    
    xtnsLeftToday()
        how many transactions left today?

DATA
    ApiKey = '1d229f72ad6b7027408bd5957cb8b31df6a812a5'
    LOG = <open file '/tmp/kno.LOG', mode 'a+'>
    MaxResults = 2
    Pfx = 'https://gateway-a.watsonplatform.net'
    default_app = [<bottle.Bottle object at 0x109c1efd0>]
    request = <LocalRequest: GET http://127.0.0.1/>
    response = Content-Type: text/html; charset=UTF-8



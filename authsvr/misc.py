from bottle import response

def add_cors_headers():
    allow_methods = ', '.join(['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
    allow_headers = ', '.join(['Origin', 'X-Requested-With', 
                               'Content-Type',  'Accept', 'Authorization', 'Access-Token'])
    response.headers['Access-Control-Allow-Credentials'] = 'true';
    #response.headers['Access-Control-Allow-Origin']='http://url:8080'
    response.headers['Access-Control-Allow-Origin'     ] = '*'
    response.headers['Access-Control-Allow-Methods'    ] = allow_methods
    response.headers['Access-Control-Allow-Headers'    ] = allow_headers
    return ['OK']


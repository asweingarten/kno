
print "FACEBOOK"

from rauth import OAuth2Service

facebook = OAuth2Service(
    client_id='852338521552385',
    client_secret='4639dfbad1a0bf5b22198ef705c2d9c8',
    name='facebook',
    authorize_url='https://graph.facebook.com/oauth/authorize',
    access_token_url='https://graph.facebook.com/oauth/access_token',
    base_url='https://graph.facebook.com/')

print "fb0", facebook

redirect_uri = 'https://www.facebook.com/connect/login_success.html'
redirect_uri = 'http://kno.ccl.io:7777/auth/callback/fb'
params = {'scope': 'read_stream',
          'response_type': 'code',
          'redirect_uri': redirect_uri}
params = {
          'response_type': 'code',
          'redirect_uri': redirect_uri}

url = facebook.get_authorize_url(**params)

print "URL", url

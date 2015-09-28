import os, sys
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


if sys.argv[1]=='1':

    url = facebook.get_authorize_url(**params)

    print "URL", url

    # GOT:
    #http://kno.ccl.io:7777/auth/callback/fb?code=AQD2K-8Bv3Jvmr_SLjJpXRwUKEiaPjTHCk-yiukvvmGGzsAc15ZRw7udhdSjzN4MIVvyvWGH8NvbaxFjhIXd86K-i7kWLzH9lVervxNZJ5__8F0CfAkvruOXJtHGyAgE44V4DR-IIZUdc4WCNHA9hynpRRbuSD_WF74nwpFI5zppGy71BkQ6JoeFPPK-I7RRAlG9Eil5uk3kksuZZNuSUevWsvsHxgJGBGivJiNq9SRjZlko2ioBYOJk8gavEIZKI-CbiAn_TsuI3d_yywwk9mswIlf3O0xlY8SKxo95Li9CxjhyVVPr6C0y2OXZABRtntEWuVJTxz9cO_7X4OOcuh4Q0DFAbt8ZtDUu3Sntzpr70A#_=_

elif sys.argv[1]=='2':
    code = sys.argv[2]

    print "CODE", code

    session = facebook.get_auth_session(data={'code': code,
                                              'redirect_uri': redirect_uri})
    
    print session.get('me').json()

    # {u'name': u'Joel Val Ward', u'id': u'10153639132090586'}

# authsvr

> Clipped from pydoc:

Help on module authsvr:

NAME
    authsvr - simple fast persistent user authentication

FILE
    /Users/val/src/kno/authsvr/authsvr.py

DESCRIPTION
    Uses in memory lookups backed by a sqlite database
    
    All these things return the same basic format:
    
    success:
      { success: True, result: { ... } }
    
    failure:
      { success: False, error: { message: "..." } }

FUNCTIONS
    DB()
        get the static database connection
    
    addUser()
        /addUser?uid=<user_id>
        
        add in a user's access token
        
        returns: { uid: <uid> }
    
    deleteUser()
        /deleteUser?token=<auth_token>
        
        delete a user's access token
        
        returns: { uid: <uid> }
    
    verifyToken()
        /verifyToken?token=<auth_token>
        
        is "token" valid?
        if so, get some basic info like the uid
        
        returns: { uid: <uid> }

DATA
    Users = {}
    app = <bottle.Bottle object>
    request = <LocalRequest: GET http://127.0.0.1/>



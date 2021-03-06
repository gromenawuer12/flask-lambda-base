import jwt, os, sys
from functools import wraps
from flask import request
from .token_invalid_exception import TokenInvalidException


def token_required(f):  
  @wraps(f)  
  def decorator(*args, **kwargs):

      if not 'Authorization' in request.headers: 
        raise TokenInvalidException() 
      auth_username = None
      token = request.headers['Authorization'].split()[1]
      try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'),algorithms=["HS256"]) 
        auth_username =  payload['username']
      except:  
        raise TokenInvalidException()


      return f(auth_username, *args,  **kwargs)  
  return decorator
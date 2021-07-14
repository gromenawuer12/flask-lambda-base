import sys, re
from .user import User
from functools import wraps

def nose(f):  
  @wraps(f)  
  def decorator(*args, **kwargs):

      user = vars(f(*args, **kwargs))
      for key in list(user.keys()):
        if re.search(r"_(username|role|password)",key):
          new_key = key.replace("_","")
          user[new_key] = user[key]
          del user[key]

      return user
  return decorator
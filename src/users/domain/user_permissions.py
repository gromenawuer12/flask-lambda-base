from .nose_decorator import nose

def deleteAttrs(user,lAttr):
    for attr in lAttr:
        delattr(user, attr)
    return user
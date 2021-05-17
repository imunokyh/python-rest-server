import jwt

from flask import request
from functools import wraps

from models.users_model import Users

def check_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        header = request.headers.get('authorization')
        if header == None:
            result = { 'message': 'authrization failed' }, 401
        else:
            data = jwt.decode(header, 'secret', algorithm='HS256')
            id = data.get('id')
            query = Users.query.filter_by(id=id).first()
            if query.token == header:
                result = func(*args, **kwargs)
            else:
                result = { 'message': 'authrization failed' }, 401 
        return result
    return wrapper
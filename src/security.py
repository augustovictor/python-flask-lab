from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'Victor', 'aaaa')
]

def authenticate(username, password):
    user = next(filter(lambda u: u.username == username, users), None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return next(filter(lambda u: u.id == user_id, users), None)
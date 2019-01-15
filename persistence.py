import shelve
import uuid

class UserInfo:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

users = shelve.open('user')

def create_user(firstname, lastname):
    id = str(uuid.uuid4())
    user = UserInfo(firstname, lastname)
    users[id] = user

def get_user(firstname):
    klist = list(users.keys())
    for key in klist:
        user = users[key]
        if user.firstname == firstname:
            return user
    return None
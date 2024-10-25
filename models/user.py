from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, profession):
        self.id = id
        self.username = username
        self.password = password
        self.profession = profession

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    
    def get_profession(self):
        return str(self.profession)
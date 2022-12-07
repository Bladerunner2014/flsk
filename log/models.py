from log import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    email = db.Column(db.String(60), unique = True, nullable = False)
    password = db.Column(db.String(60), unique = True, nullable = False)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.username})"

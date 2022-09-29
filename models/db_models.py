from dependencies import *


class DBUser(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    role = db.Column(db.String(1000))


@login_manager.user_loader
def load_user(user_id):
    return DBUser.query.get(int(user_id))

from dependencies import *

class DBUser(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))
    verified = db.Column(db.Boolean(), default="False")


class DBDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100),unique=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    date_of_birth = db.Column(db.String(100))
    pincode = db.Column(db.String(100))
    country = db.Column(db.String(100))
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    address1 = db.Column(db.String(100))
    address2 = db.Column(db.String(100))
    address3 = db.Column(db.String(100))
    landmark = db.Column(db.String(100))
    userpic = db.Column(db.String(100))
    contact_primary = db.Column(db.String(100), unique=True)
    gems = db.Column(db.String(100))


@login_manager.user_loader
def load_user(user_id):
    return DBUser.query.get(int(user_id))

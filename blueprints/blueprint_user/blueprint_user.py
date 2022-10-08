from dependencies import *
from models.db_models import DBDetails, DBUser

blueprint_user = Blueprint('blueprint_user', __name__)


@blueprint_user.route("/login")
def login():
    if(current_user.is_authenticated):
        return redirect(url_for('blueprint_utilities.home'))
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    data = {

    }
    data["user"] = current_user
    responseTemplate["data"] = data
    return render_template("login/login.htm", res=responseTemplate)


@blueprint_user.route("/login", methods=['POST'])
def login_auth():
    data = request.json

    email = data["email"]
    password = data["password"]

    user = DBUser.query.filter_by(email=email).first()

    result = {
        "status": "",
        "message": ""
    }

    if not user or not check_password_hash(user.password, password):
        print('USERNAME or PASSWORD INCORRECT')
        result["status"] = "401"
        result["message"] = "Username or password is Incorrect"
        return jsonify(result)

    result["status"] = "200"
    result["message"] = "Authorization Successfull"

    login_user(user, remember=True)

    return jsonify(result)


@blueprint_user.route("/signup")
def signup():
    if(current_user.is_authenticated):
        return redirect(url_for('blueprint_utilities.home'))
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    data = {

    }
    data["user"] = current_user
    responseTemplate["data"] = data
    return render_template("signup/signup.htm", res=responseTemplate)


@blueprint_user.route("/signup", methods=['POST'])
def signup_auth():
    data = request.json

    email = data["email"]
    role = data["role"]
    password = data["password"]
    user_id = str(uuid.uuid4())

    user = DBUser.query.filter_by(email=data["email"]).first()

    result = {
        "status": "",
        "message": ""
    }

    if(user):
        print("User already exists")
        result["status"] = "401"
        result["message"] = "Email already registered"
        return jsonify(result)

    new_user = DBUser(user_id=user_id, email=email, role=role, password=generate_password_hash(
        password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    result["status"] = "200"
    result["message"] = "Signup Successfull"
    return jsonify(result)


@blueprint_user.route("/settings")
@login_required
def settings():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    data = {

    }
    data["states"] = STATES
    data["countries"] = COUNTRIES
    data["user"] = current_user
    responseTemplate["data"] = data
    return render_template("settings/settings.htm", res=responseTemplate)


@blueprint_user.route("/settings", methods=["POST"])
@login_required
def update_settings():
    result = {
        "status": "",
        "message": ""
    }

    if(current_user.is_authenticated() == False):
        result["status"] = "401"
        result["message"] = "Access denied"
        return jsonify(result)

    data = request.json

    name = data["name"]
    username = data["username"]
    email = data["email"]
    dob = data["dob"]
    pincode = data["pincode"]
    country = data["country"]
    state = data["state"]
    city = data["city"]
    address1 = data["address1"]
    address2 = data["address2"]
    address3 = data["address3"]
    landmark = data["landmark"]

    user_details = DBDetails.query.filter_by(email=current_user.email).first()

    result["status"] = "200"
    result["message"] = "Updated Successfully"
    return jsonify(result)


@blueprint_user.route("/profile")
@login_required
def profile():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    data = {

    }
    data["user"] = current_user
    responseTemplate["data"] = data
    return render_template("profile/profile.htm", res=responseTemplate)


@blueprint_user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('blueprint_user.login'))


@blueprint_user.route("/notifications")
@login_required
def notifications():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    data = {

    }
    data["user"] = current_user
    responseTemplate["data"] = data
    return render_template("notifications/notifications.htm", res=responseTemplate)

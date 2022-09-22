from dependencies import *

blueprint_user = Blueprint('blueprint_user', __name__)


@blueprint_user.route("/login")
def login():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    responseTemplate["errorMsg"] = "Username or Password is wrong"
    return render_template("login/login.htm", res=responseTemplate)


@blueprint_user.route("/signup")
def signup():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    responseTemplate["errorMsg"] = "Username/Email/Phone already exists"
    return render_template("signup/signup.htm", res=responseTemplate)


@blueprint_user.route("/settings")
def settings():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    responseTemplate["states"] = STATES
    responseTemplate["countries"] = COUNTRIES
    return render_template("settings/settings.htm", res=responseTemplate)


@blueprint_user.route("/profile")
def profile():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("profile/profile.htm", res=responseTemplate)


@blueprint_user.route("/logout")
def logout():
    return redirect(url_for('blueprint_user.login'))


@blueprint_user.route("/notifications")
def notifications():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("notifications/notifications.htm", res=responseTemplate)

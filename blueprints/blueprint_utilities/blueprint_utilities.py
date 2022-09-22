from dependencies import *

blueprint_utilities = Blueprint(
    "blueprint_utilities", __name__)


@blueprint_utilities.route("/")
def home():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    responseTemplate["stats"] = [['100+', 'Subjects'],
                                 ['100+', 'Skills'], ['1K+', 'Teachers']]
    return render_template("home/home.htm", res=responseTemplate)


@blueprint_utilities.route("/careers")
def careers():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("careers/careers.htm", res=responseTemplate)


@blueprint_utilities.route("/contact-us")
def contact_us():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("contact-us/contact-us.htm", res=responseTemplate)


@blueprint_utilities.route("/help")
def help():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("help/help.htm", res=responseTemplate)

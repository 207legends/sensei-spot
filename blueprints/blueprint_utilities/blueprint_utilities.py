from flask import Blueprint, request, render_template, redirect, url_for
from run import responseTemplate

blueprint_utilities = Blueprint("blueprint_utilities",__name__,static_folder='static', template_folder='templates')

@blueprint_utilities.route("/")
def home():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
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

from urllib import response
from flask import Flask, render_template, request, jsonify
import json

PATH_API = "/api/v1/"

test = False

path = ''

if (test == False):
    path = '/home/sensiespot/mysite/sensei-spot/'

with open(path + 'data/places/countries.json', encoding="utf8") as f:
    dataCountries = json.load(f)

COUNTRIES = []

for i in dataCountries:
    COUNTRIES.append(i["name"])

with open(path + 'data/places/states.json', encoding="utf8") as f:
    dataStates = json.load(f)

STATES = {}

for i in dataStates:
    c = i["country_name"]
    s = i["name"]
    if c not in STATES:
        STATES[c] = [s]
    else:
        STATES[c].append(s)


with open(path + 'data/places/cities.json', encoding="utf8") as f:
    dataCities = json.load(f)

CITIES = {}

for i in dataCities:
    s = i["state_name"]
    c = i["name"]
    if s not in CITIES:
        CITIES[s] = [c]
    else:
        CITIES[s].append(c)

app = Flask(__name__)


responseTemplate = {
    "app-theme": "light",
    "app-name": "Sensei Spot",
    "app-top-announcement": "Need a solution -> Think of a Sensie",
}


@app.route("/")
def home():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("home/home.htm", res=responseTemplate)


@app.route("/login")
def login():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    responseTemplate["errorMsg"] = "Username or Password is wrong"
    return render_template("login/login.htm", res=responseTemplate)


@app.route("/signup")
def signup():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    responseTemplate["errorMsg"] = "Username/Email/Phone already exists"
    return render_template("signup/signup.htm", res=responseTemplate)


@app.route("/careers")
def careers():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("careers/careers.htm", res=responseTemplate)


@app.route("/contact-us")
def contact_us():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("contact-us/contact-us.htm", res=responseTemplate)


@app.route("/settings")
def settings():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    responseTemplate["states"] = STATES
    responseTemplate["countries"] = COUNTRIES
    return render_template("settings/settings.htm", res=responseTemplate)


@app.route("/trending-dishes-all")
def trending_dishes_all():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("trending-dishes-all/trending-dishes-all.htm", res=responseTemplate)


@app.route("/trending-shops-all")
def trending_shops_all():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("trending-shops-all/trending-shops-all.htm", res=responseTemplate)


@app.route("/profile")
def profile():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("profile/profile.htm", res=responseTemplate)


@app.route("/help")
def help():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("help/help.htm", res=responseTemplate)


@app.route("/logout")
def logout():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("login/login.htm", res=responseTemplate)


@app.route("/menu")
def menu():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("menu/menu.htm", res=responseTemplate)


@app.route(PATH_API + "/countries", methods=['GET'])
def getCountries():
    if (request.method == 'GET'):
        res = {
            "countries": COUNTRIES
        }

    return jsonify(res)


@app.route(PATH_API + "/<country>/states", methods=['GET'])
def getStatesFromCountry(country):
    if (request.method == 'GET'):
        if country in STATES:
            res = {
                "country": country,
                "states": STATES[country]
            }
        else:
            res = {
                "country": country,
                "states": []
            }

    return jsonify(res)


@app.route(PATH_API + "/<country>/<state>/cities", methods=['GET'])
def getCitiesFromState(country, state):
    if (request.method == 'GET'):
        if state in CITIES:
            res = {
                "country": country,
                "state": state,
                "cities": CITIES[state]
            }
        else:
            res = {
                "country": country,
                "state": state,
                "cities": []
            }

    return jsonify(res)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('utilities/404page/404page.htm', res=responseTemplate), 404


if __name__ == "__main__":
    app.run(debug=True)

from flask import render_template, request, jsonify
from run import app, responseTemplate, COUNTRIES, CITIES, STATES
from blueprints.blueprint_user.blueprint_user import blueprint_user

PATH_API = "/api/v1/"


@app.route("/")
def home():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("home/home.htm", res=responseTemplate)


@app.route("/careers")
def careers():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("careers/careers.htm", res=responseTemplate)


@app.route("/contact-us")
def contact_us():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("contact-us/contact-us.htm", res=responseTemplate)


@app.route("/trending-dishes-all")
def trending_dishes_all():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("trending-dishes-all/trending-dishes-all.htm", res=responseTemplate)


@app.route("/trending-shops-all")
def trending_shops_all():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("trending-shops-all/trending-shops-all.htm", res=responseTemplate)


@app.route("/help")
def help():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("help/help.htm", res=responseTemplate)


@blueprint_user.route("/logout")
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
    app.register_blueprint(blueprint_user, url_prefix="/user")
    app.run(debug=True)

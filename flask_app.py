from dependencies import *

@app.route("/trending-dishes-all")
def trending_skills_all():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("trending-dishes-all/trending-dishes-all.htm", res=responseTemplate)


@app.route("/trending-shops-all")
def trending_shops_all():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("trending-shops-all/trending-shops-all.htm", res=responseTemplate)


@app.route("/menu")
def menu():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    return render_template("menu/menu.htm", res=responseTemplate)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('utilities/404page/404page.htm', res=responseTemplate), 404


if __name__ == "__main__":
    app.register_blueprint(blueprint_user, url_prefix="/user")
    app.register_blueprint(blueprint_utilities, url_prefix="")
    print(PATH_API + "places")
    app.register_blueprint(api_places, url_prefix=PATH_API+"places")
    app.run(debug=True)

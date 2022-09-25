from dependencies import *
from blueprints_all import *

app.register_blueprint(blueprint_user, url_prefix="/user")
app.register_blueprint(blueprint_utilities, url_prefix="")
app.register_blueprint(api_places, url_prefix=PATH_API+"places")
app.register_blueprint(blueprint_sensei, url_prefix="")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('utilities/404page/404page.htm', res=responseTemplate), 404


if __name__ == '__main__':
    app.run(debug=True)

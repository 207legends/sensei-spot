from dependencies import *

blueprint_sensei_all = Blueprint('blueprint_sensei_all', __name__)

@blueprint_sensei_all.route('/sensei-all')
def sensei_all():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    responseTemplate["countries"] = COUNTRIES
    return render_template('sensei-all/sensei-all.htm',res = responseTemplate)
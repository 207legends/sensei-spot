from dependencies import *
from models.dummy_models import dummySensei

blueprint_sensei = Blueprint('blueprint_sensei', __name__)


@blueprint_sensei.route('/sensei-all')
def sensei_all():
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    data = {

    }
    data["user"] = current_user
    data["countries"] = COUNTRIES
    responseTemplate["data"] = data
    return render_template('sensei-all/sensei-all.htm', res=responseTemplate)


@blueprint_sensei.route('/sensei/<username>')
def sensei_user(username):
    responseTemplate["app-theme"] = request.cookies.get('app-theme')
    data = {

    }
    data["user"] = current_user
    data["countries"] = COUNTRIES
    data["sensei"] = dummySensei
    responseTemplate["data"] = data
    return render_template('sensei-profile/sensei-profile.htm', res=responseTemplate)

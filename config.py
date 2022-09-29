from imports_all import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'navi17101999'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'blueprint_user.login'
login_manager.init_app(app)

PATH_API = "/api/v1/"

responseTemplate = {
    "app-theme": "light",
    "app-name": "Sensei Spot",
    "app-top-announcement": "Need a solution -> Think of a Sensei",
}

#path = '/home/sensiespot/mysite/sensei-spot/'
path = os.getcwd() + '/'

with open(path + 'data/places/countries.json', encoding="utf8") as f:
    dataCountries = json.load(f)

COUNTRIES = []
STATES = {}
CITIES = {}

for i in dataCountries:
    COUNTRIES.append(i["name"])

with open(path + 'data/places/states.json', encoding="utf8") as f:
    dataStates = json.load(f)

for i in dataStates:
    c = i["country_name"]
    s = i["name"]
    if c not in STATES:
        STATES[c] = [s]
    else:
        STATES[c].append(s)


with open(path + 'data/places/cities.json', encoding="utf8") as f:
    dataCities = json.load(f)

for i in dataCities:
    s = i["state_name"]
    c = i["name"]
    if s not in CITIES:
        CITIES[s] = [c]
    else:
        CITIES[s].append(c)

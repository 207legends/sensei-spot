from flask import Flask
import json
import os

app = Flask(__name__)

PATH_API = "/api/v1/"

responseTemplate = {
    "app-theme": "light",
    "app-name": "Sensei Spot",
    "app-top-announcement": "Need a solution -> Think of a Sensie",
}

path = ''
#path = os.getcwd() + '/'

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

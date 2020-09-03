from flask import Flask,jsonify;
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

url = 'https://coronavirus-19-api.herokuapp.com'

@app.route('/cases')
def get_all_cases():
    cases = requests.get(url + '/countries').json()
    return jsonify(cases)

@app.route('/cases/<country>')
def get_cases_by_country(country):
    cases = requests.get(url + '/countries/' + country).json()
    return jsonify(cases)

@app.route('/<country>/active')
def get_active_cases(country):
    cases = requests.get(url + '/countries/' + country).json()
    return jsonify(cases['active'])

@app.route('/<country>/cases')
def get_total_cases(country):
    cases = requests.get(url + '/countries/' + country).json()
    return jsonify(cases['cases'])

@app.route('/<country>/deaths')
def get_death_cases(country):
    cases = requests.get(url + '/countries/' + country).json()
    return jsonify(cases['deaths'])

@app.route('/<country>/recovered')
def get_recovered_cases(country):
    cases = requests.get(url + '/countries/' + country).json()
    return jsonify(cases['recovered'])
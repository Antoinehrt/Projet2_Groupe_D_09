from flask import Flask, render_template, jsonify
from urllib.request import urlretrieve as retrieve
import csv


def get_file():
    url = 'https://covid.ourworldindata.org/data/ecdc/total_cases.csv'
    retrieve(url, 'total_cases.csv')


def import_csv(filename):
    """
    :type filename: 'filename.CSV'
    """
    with open(filename, 'r') as file:
        fileCSV = csv.reader(file)
        lstX = []
        lstY = []
        lstBelgium = []
        for line in fileCSV:
            if type(line[0]) == str:
                lstX.append(line[0])
                lstY.append(line[1])
                lstBelgium.append(line[17])
            else:
                lstX.append(float(line[0]))
                lstY.append(float(line[1]))
                lstBelgium.append(float(line[17]))

        return lstX, lstY, lstBelgium


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("date")
def date():
    x = import_csv('total_cases.csv')
    d = x[0][1:]
    return jsonify({'date': d})


@app.route("data_Y")
def data_Y():
    x = import_csv('total_cases.csv')
    d = x[1][1:]
    return jsonify({'date': d})


@app.route("data_Belgium")
def data_Belgium():
    x = import_csv('total_cases.csv')
    d = x[2][1:]
    return jsonify({'date': d})


if __name__ == "__main__":
    app.run(debug=True)

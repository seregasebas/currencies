import requests
import json
from flask import Flask

def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    text = '<h1 style="color: red; border-width: 3; border-color: red;  border-style: ridge; text-align: center">Курс валют</h1>'
    text += '<table align="center">'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr style="color:rgb(2,87,255)">'
        for v in valute.values():
            text += f'<td style="border-width: 1; border-color: gray;  border-style: solid; text-align: center">{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html

if __name__ == "__main__":
    app.run()
import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template

import requests
import pandas as pd
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='static/uploads'

url = "https://fantasy.premierleague.com/api/bootstrap-static/"

r = requests.get(url)
json = r.json()
json.keys()
events_df = pd.DataFrame(json['events'])

@app.route('/', methods=("POST", "GET"))
def new_table():

    return render_template('new.html',  tables=[events_df.to_html(classes='data')], titles=events_df.columns.values)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True,threaded=True)

    app.debug = True
    app.run()

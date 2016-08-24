from flask import Flask, request
import urllib

import dill
import pandas as pd

f = urllib.request.urlopen("https://github.com/crawles/sentiment_analysis_twitter_model/raw/master/twitter_sentiment_model.pkl")
cl = dill.load(f)
f.close()

app = Flask(__name__)
@app.route('/identify', methods=['POST'])
def sentiment_compute():
    req = request.get_json(force=True)
    print(req)
    prediction = cl.predict_proba(req['data'])[:][:,1]
    return(str(prediction))

app.run(debug = True)

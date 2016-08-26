# -*- coding: utf-8 -*-

'''
sentiment_service.py
~~~~~~~~~~~~~~~~~~~~

App implements a pre-trained sentiment analysis pipeline. 

'''
import os

import dill
from flask import Flask, request, jsonify
import pandas as pd
import requests
import sklearn

resp = requests.get("https://github.com/crawles/sentiment_analysis_twitter_model/raw/master/twitter_sentiment_model.pkl")
resp.raise_for_status()
cl = dill.loads(resp.content)

app = Flask(__name__)

@app.route('/polarity_compute', methods=['POST'])
def sentiment_compute():
    req = request.get_json(force=True)
    prediction = cl.predict_proba(req['data'])[:][:,1]
    return(jsonify({"polarity" : prediction.tolist()}))

if __name__ == "__main__":
    if os.environ.get('VCAP_SERVICES') is None: # running locally
        PORT = 8080
        DEBUG = True
    else:                                       # running on CF
        PORT = int(os.getenv("PORT"))
        DEBUG = False

    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)

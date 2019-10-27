# -*- coding: utf-8 -*-

'''
sentiment_service.py
~~~~~~~~~~~~~~~~~~~~

App implements a sentiment analysis pipeline. 

'''
import cPickle
import os

from flask import Flask, request, jsonify
import pandas as pd
import sklearn

model = open("twitter_sentiment_model.pkl", "r")
cl = cPickle.loads(model.read())

def regex_preprocess(raw_tweets):
    pp_text = pd.Series(raw_tweets)
    
    user_pat = '(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)'
    http_pat = '(https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})'
    repeat_pat, repeat_repl = "(.)\\1\\1+",'\\1\\1'

    pp_text = pp_text.str.replace(pat = user_pat, repl = 'USERNAME')
    pp_text = pp_text.str.replace(pat = http_pat, repl = 'URL')
    pp_text.str.replace(pat = repeat_pat, repl = repeat_repl)
    return pp_text

app = Flask(__name__)

@app.route('/polarity_compute', methods=['POST'])
def sentiment_compute():
    req = request.get_json(force=True)
    X = regex_preprocess(req['data'])
    prediction = cl.predict_proba(X)[:][:,1]
    return(jsonify({"polarity" : prediction.tolist()}))

if __name__ == "__main__":
    if os.environ.get('VCAP_SERVICES') is None: # running locally
        PORT = 8080
        DEBUG = True
    else:                                       # running on CF
        PORT = int(os.getenv("PORT"))
        DEBUG = False

    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)

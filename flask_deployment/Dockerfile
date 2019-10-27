FROM python:2.7

WORKDIR /app

COPY sentiment_service.py .

RUN wget https://raw.githubusercontent.com/crawles/gpdb_sentiment_analysis_twitter_model/master/twitter_sentiment_model.pkl \
 && pip install gunicorn flask pandas sklearn

EXPOSE 80

CMD gunicorn --bind 0.0.0.0:80 sentiment_service:app

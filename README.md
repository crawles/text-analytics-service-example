##Example: Text analytics as a service
Example for deploying a Twitter sentiment analysis microservice accessible via an API. There are two implementatations using 
* Jupyter Notebook (via the [Jupyter Kernel Gateway](https://github.com/jupyter/kernel_gateway))
* Flask

Both apps are deployed on Cloud Foundry.

Both implementations use this [sentiment classifier](https://github.com/crawles/sentiment_analysis_twitter_model). The classifier is based on the approach of [Go et al](http://cs.stanford.edu/people/alecmgo/papers/TwitterDistantSupervision09.pdf) using the [Sentiment140 data](http://help.sentiment140.com/for-students/)

### Requirements
* Cloud Foundry

### Deploying the classifier
#### Jupyter Notebook Microservice
```
cd jupyter_gateway_deployment
cf push
```
#### Flask Microservice
```
cd flask_deployment
cf push
```
### Using the classifier via the API
The classifier accepts POST requests of text:
```
curl -H "Content-Type: application/json" -X POST -d '{"data":["This app is awesome and in the CLOUD","Steph Curry is a basketball player","i am so mad and angry"]}' sentiment-compute.cfapps.pez.pivotal.io/polarity_compute
```

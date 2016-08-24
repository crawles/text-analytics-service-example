##Example: Text Analytics as a Service
Example for deploying a machine learning model for analyzing text. The example deploys a Twitter sentiment classifier as a microservice accessible via an API POST request. There are two implementatations of deploying the model using 
* Jupyter Notebook (via the [Jupyter Kernel Gateway](https://github.com/jupyter/kernel_gateway))
* Flask

Both apps are deployed on Cloud Foundry.

Both implementations use this [sentiment classifier](https://github.com/crawles/sentiment_analysis_twitter_model). The classifier is based on the approach of [Go et al](http://cs.stanford.edu/people/alecmgo/papers/TwitterDistantSupervision09.pdf) using the [Sentiment140 data](http://help.sentiment140.com/for-students/)

### Requirements
* Cloud Foundry

If you do not have an account on a Cloud Foundry installation you can register for a free trial at [Pivotal Web Services (PWS)](http://run.pivotal.io).

Download the Cloud Foundry Command Line Interface from the CF management console
or [the CF Github repo](https://github.com/cloudfoundry/cli).
This provides the `cf` command which you will use to interact with a CF installation.

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
The classifier accepts POST requests of text and returns a polarity prediction from 0 to 1. Lower polarity indicates negative sentiment and higher polarity indicates positive sentiment.
```
$ curl -H "Content-Type: application/json" -X POST -d '{"data":["This app is awesome and in the CLOUD","Steph Curry is a basketball player","i am so mad and angry"]}' sentiment-compute-flask.cfapps.pez.pivotal.io/polarity_compute
{
  "polarity": [
    0.7803128570201056,
    0.49108974839197184,
    0.14809403223487322
  ]
}
```
### Resources

* [Sentiment classifier](https://github.com/crawles/sentiment_analysis_twitter_model)
* [Python Cloud Foundry examples](https://github.com/ihuston/python-cf-examples)
* [Cloud Foundry Documentation](https://github.com/ihuston/python-cf-examples)
* Pivotal Blog: [Model scoring as a service](https://blog.pivotal.io/data-science-pivotal/products/scoring-as-a-service-to-operationalize-algorithms-for-real-time)

### Author

`Chris Rawles`

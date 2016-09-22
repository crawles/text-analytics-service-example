##Example: Text Analytics as a Service
This example deploys a Twitter sentiment classifier as a microservice accessible via an API `POST` request. The classifier was built using PL/Python in Greenplum Database (GPDB). 

Read this [blog post](https://blog.pivotal.io/data-science-pivotal/case-studies/data-science-how-to-text-analytics-as-a-service) for more information.

There are two implementatations of deploying the model using 
* Jupyter Notebook (via the [Jupyter Kernel Gateway](https://github.com/jupyter/kernel_gateway))
* Flask

Both apps are deployed on Cloud Foundry. This example deploys a trained sentiment classifier, but this framework can be modified for additional text analytics and general data science tasks.

Both implementations use [this sentiment classifier](https://github.com/crawles/gpdb_sentiment_analysis_twitter_model) which was built in a massively parallel processing environment using GPDB. The classifier is based on the approach of [Go et al](http://cs.stanford.edu/people/alecmgo/papers/TwitterDistantSupervision09.pdf) using the [Sentiment140 data](http://help.sentiment140.com/for-students/)

### Deploying to Cloud Foundry

If you do not have an account on a Cloud Foundry installation you can register for a free trial at [Pivotal Web Services (PWS)](http://run.pivotal.io). 

Download the Cloud Foundry Command Line Interface from the CF management console
or [the CF Github repo](https://github.com/cloudfoundry/cli).
This provides the `cf` command which you will use to interact with a CF installation.

Alternatively, you can install [PCF Dev](https://github.com/pivotal-cf/pcfdev) to install Cloud Foundry on a single work station.

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
The classifier accepts `POST` requests of text and returns a polarity prediction from 0 to 1. Lower polarity indicates negative sentiment and higher polarity indicates positive sentiment.
```
$ curl -H "Content-Type: application/json" -X POST -d '{"data":["This app is awesome and in the CLOUD","Steph Curry is a basketball player","i am so mad and angry"]}' sentiment-compute-flask.cfapps.pez.pivotal.io/polarity_compute
```
```
# returned result
{
  "polarity": [
    0.7803128570201056,
    0.49108974839197184,
    0.14809403223487322
  ]
}
```

Examples of both apps are currently deployed and be accessed at:

```
sentiment-compute.cfapps.pez.pivotal.io/polarity_compute
```
```
sentiment-compute-flask.cfapps.pez.pivotal.io/polarity_compute
```

### Resources

* [Sentiment classifier](https://github.com/crawles/gpdb_sentiment_analysis_twitter_model)
* [Python Cloud Foundry examples](https://github.com/ihuston/python-cf-examples)
* [Cloud Foundry Documentation](https://docs.cloudfoundry.org/)
* Pivotal Blog: [Model scoring as a service](https://blog.pivotal.io/data-science-pivotal/products/scoring-as-a-service-to-operationalize-algorithms-for-real-time)

### Author

`Chris Rawles`

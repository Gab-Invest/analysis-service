## Analysis Service

The analysis service is responsible for collecting Twitter metrics for a company, conducting analysis through the use of some AI tool, and then returning this analysis in real-time to the application.

## Project's structure

Given that the service has a specific function within a large system, it is proposed to use a simple architecture while maintaining good system design practices and following **SOLID** principles for code organization.
 
The following diagram presents the folder organization that's be used by this project:

![folders](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/89d67dac-c733-4ea3-bf1f-528854d84547/metricas_pacote.drawio.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230325T033509Z&X-Amz-Expires=86400&X-Amz-Signature=5517744773d8c76a21a9f4e6c83ab125adcd4adc61680eaeaaa5cc4a3783d54e&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22metricas%2520pacote.drawio.png%22&x-id=GetObject)

## Technologies:

- [RabbitMQ](https://www.rabbitmq.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [snscrape](https://github.com/JustAnotherArchivist/snscrape)
- [NLTK](https://www.nltk.org/)
- [pandas](https://pandas.pydata.org/)
- [pytest](https://docs.pytest.org/en/7.2.x/)

## Config

### Requirements

Before running the project you must have installed:

- [Docker](https://www.docker.com/)


### Env 

````
# Server
PORT=

# RabbitMQ
RABBITMQ_DEFAULT_USER=
RABBITMQ_DEFAULT_PASS=
````

## Running the project

To run the project, go to the root of the project and then run:

- running the project for the first time: 

````
make build
````

- running the project in other occasions: 

````
make up
````

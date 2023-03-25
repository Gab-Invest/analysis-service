## Analysis Service

The analysis service is responsible for collecting Twitter metrics for a company, conducting analysis through the use of some AI tool, and then returning this analysis in real-time to the application.

## Project's structure

Given that the service has a specific function within a large system, it is proposed to use a simple architecture while maintaining good system design practices and following **SOLID** principles for code organization.
 
The following diagram presents the folder organization that's be used by this project:

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
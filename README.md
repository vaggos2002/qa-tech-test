# qa-tech-test
QA Tech test challenge

## Introduction

The proposed *testing framework* was created having in mind that :

- (1) these test cases will need to be further developed and maintained using 
  a developer-friendly i.e. Postman and
- (2) the test cases should be possible to be executed in a CICD pipeline 
  using isolated Docker containers  

The existed code of the app was moved inside the repository for convenience, however
it could be alternatively be in a separate repository.

The solution was created using *Postman 6.7.1* on *OSX Sierra 10.12.6*.

### Postman - Newman
The test cases were developed using the Postman's tests feature. These tests are
writen in Javascript language. The test collection can be found at *tests/*.

*Newman* is the command line collection runner for Postman test cases and it is
used to execute the postman test cases from inside the docker container.

The test cases use environment variables as defined at *tests/docker_environment.json*
and *docker_global.json* and they are loaded at the newman command line
. For instance the *hostname* defines the hostname of the REST API server and it is
set to be equal to *app* when running the tes cases inside the container. 

### Docker Compose
Docker Compose is a tool allowing to run multiple container Docker applications. 

Two docker contains were defined at the *docker-compose.yml*,

- *app* that uses a lightweight Alphine Linux image (python:3.6-alpine) with 
  pre-installed python 3.6. The container installs the app requirements, populates
  the database and then starts the app. Only the 5000 port is exposed to the docker
  host and the *newman* container. 
- *newman* container uses an Ubuntu image (postman/newman:ubuntu) with a
  pre-installed npm, postman and newman modules. The container waits the *app* container
  to be fired up before it starts. 


## Requirements

The testing framework can operate in any UNIX operating system (e.g. GNU/Linux, MacOS X)

- [Docker Compose](https://docs.docker.com/compose/install/)
- [Postman](https://www.getpostman.com/downloads/)

## To develop/maintain the test cases

1. Build the docker containers ```$ docker-compose build --no-cache```

2. Run the app only with detached mode (-d) i.e. run containers in the 
   background, print new container names : ```$ docker-compose up -d app```

3. Load the test cases *tests/collection.json* to postman and update the test cases.

4. Shut-down the containers ```docker-compose stop```

## In CI

To run the app and the tests, the following command need to be executed:
```$ docker-compose up --abort-on-container-exit```

The command fires up two docker containers (a) contains the app and (b)
with newman installed. The postman test collection are executed at the newman container
and the container exits halting the app container as well.

With the following command it is possible to get the exit code of the newman container :
```docker inspect qatechtest_newman_1 --format='{{.State.ExitCode}}'```


### Future work and ideas for CI

The use of an HTML report would be great idea to visualise the test results using the 
[newman-reporter-html](https://github.com/postmanlabs/newman-reporter-html) library. 


## Found issues

1. The method *POST /product* when the price field receives invalid characters e.g alphabetical,
   it causes the app to crash returning a *sqlalchemy.exc.StatementError* .
2. As a result of the issue 1, any following requests fail with a *sqlalchemy.exc.InvalidRequestError*.
   a work around is to restart the server.


## References

1. https://www.chaijs.com/api/bdd/ assertion library
2. https://github.com/postmanlabs/newman, newman CLI documentation
3. https://github.com/postmanlabs/newman/tree/develop/docker newman docker image documentation

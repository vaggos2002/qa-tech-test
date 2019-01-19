# qa-tech-test
QA Tech test challenge

## Introduction

Docker Compose is a tool allowing to run multiple container Docker applications. 

Two docker contains were defined, one 

These tests were created using *Postman 6.7.1* on *OSX Sierra 10.12.6*.

### Used Tools

Postman

Newman

Docker-compose


## To develop/maintain the code

1. Run the app only with detached mode (-d) i.e. run containers in the 
   background, print new container names : ```$ docker-compose up -d app```

2. Load the test cases *tests/collection.json* to postman and update the test cases.

3. Shut-down the containers ```docker-compose stop```

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

## References

1. https://www.chaijs.com/api/bdd/ assertion library
2. https://github.com/postmanlabs/newman, newman CLI documentation
3. https://github.com/postmanlabs/newman/tree/develop/docker newman docker image documentation

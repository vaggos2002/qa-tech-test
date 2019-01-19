# qa-tech-test
QA Tech test challenge

## Introduction

Docker Compose is a tool allowing to run multiple container Docker applications. 

Two docker contains were defined, one 



## To develop/maintain the code

1. Run the app only with detached mode (-d): Run containers in the background, print new container names.

```
$ docker-compose -f docker-compose.yml up -d app

```

2. To shut-down the containers ```docker-compose stop```


## In CI

To run the app and the tests, the following command need to be executed:
```$ docker-compose up --abort-on-container-exit```


### Future work / ideas

The use of an HTML report would be great idea to visualise the test results using the 
[newman-reporter-html](https://github.com/postmanlabs/newman-reporter-html) library. 


## References

1. https://www.chaijs.com/api/bdd/ assertion library
2. https://github.com/postmanlabs/newman, newman CLI documentation
3. https://github.com/postmanlabs/newman/tree/develop/docker newman docker image documentation

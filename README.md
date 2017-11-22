# README #

Small project created for learning to set up a back-bone for a distributed task processing
system. Uses Celery with RabbitMQ as a message broker, Redis as a task-storage backend,
PostgreSQL to store jobs and Django, all of which are run on Docker
containers using docker-compose.
The settings I used for Celery seemed reasonable for this simple use-case,
but I intend to explore the additional settings in the [documentation](http://docs.celeryproject.org/en/latest/userguide/configuration.html)
as this project evolves.
Based on [this](https://github.com/ilonajulczuk/docker-django-celery) example.

### Set up and running ###
- install docker and docker-compose
- from the folder where docker-compose.yml is located run:

    ```
    $ docker-compose build                                                                                                           
    $ docker-compose up
    ```  
- access the browsable API at 127.0.0.1:8000 and go to 127.0.0.1:8000/jobs/ to start tasks

### Available tasks ###
- map_url - takes a url as a string and parses its content using Beautiful soup, returning a
  word-count dictionary
- merge_maps - takes a list of word-count dictionaries and returns them merged into
  a single merged dictionary

### TODOS: ###
* write tests
* experiment with additional long-running tasks
* experiment scaling with more container instances for celery workers

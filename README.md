# todo-app
## simple CRUD django-based web-app with postgresql

How to use:
Repo is ready almost ready to use.

First of all run:

```
docker-compose up
```

Docker created two connected containers: web app and postgresql database. Docker-compose up created "Data" folder in your local repo. This is where postgresql keeps the database. Stopping the containers and composing down your images won't exterminate gathered data. Next time you run the app every task you added will be here because db is being persisted.

Now you have to migrate django models to your database. You can do it two ways:

1. In container's built-in Docker terminal:
```
python manage.py makemigrations
```
And then:
```
python manage.py migrate
```

2. Other terminal - Docker's container runs separatedly so we have to run command inside Docker.
```
docker exec -it (here goes your web-app ID from Docker without these brackets) python manage.py makemigrations
```
And then run:
```
docker exec -it (here goes your web-app ID from Docker without these brackets) python manage.py migrate
```

At this moment app is working correctly!

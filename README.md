# cours_ml_scaling

Lien du tuto pour ce projet : https://testdriven.io/courses/fastapi-celery/getting-started/

## Structure du projet

```
├── .env
│   └── .dev-sample
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 38c6e5303b49_.py
│       └── 512d31e06401_.py
├── alembic.ini
├── celerybeat-schedule
├── compose
│   └── local
│       └── fastapi
│           ├── Dockerfile
│           ├── celery
│           │   ├── beat
│           │   │   └── start
│           │   ├── flower
│           │   │   └── start
│           │   └── worker
│           │       └── start
│           ├── entrypoint
│           └── start
├── docker-compose.yml
├── main.py
├── proj
│   ├── __init__.py
│   ├── celery_utils.py
│   ├── config.py
│   ├── database.py
│   └── users
│       ├── __init__.py
│       ├── models.py
│       └── tasks.py
└── requirements.txt
```

## Lancer le projet 

Build le projet
```
docker-compose build
```
Lancer les containers
```
docker-compose up -d
```


## Tester le projet 
Run le service web
```
docker-compose exec web python
```
Test avec une simple tâche
```
>>> from main import app
>>> from project.users.tasks import divide
>>>
>>> divide.delay(1, 2)
```
Ouvrir un nouveau terminal, se placer dans le dossier du projet, et regarder les logs du worker Celery
```
docker-compose logs celery_worker
```
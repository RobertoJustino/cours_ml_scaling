# cours_ml_scaling

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
├── project
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
docker-compose build
```


## Tester le projet 


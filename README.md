# Skeleton for Django with mySQL on Docker

You can use this to quickly get started with developing for Django with mySQL on Docker. The
purpose of this skeleton is, to make this as hassle-free as possible, avoiding race-conditions
etc. so you can concentrate on development and not container orchestration, cos let's be honest
... Docker s*cks.

The docker-compose.yml will set everything up for you, so you are running with two containers,
one having Django and the other running mySQL. There is an entrypoint script, that makes sure
to wait until the database really is there before starting Django.

So just run `docker-compose up`, wait some time, and then you can connect to Django via
`http://localhost:8000`, mySQL is mapped to `localhost:3308`

The root directory of this project will be mapped into the Django container, so every code change
you make will be immediately active in the container.

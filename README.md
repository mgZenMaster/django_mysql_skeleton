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

To use this for your own projects, just replace the string `myapp` all over the project with your application name.
Also replace the string `djproj` all over the code with your project name.
It is safe to do this via a script.

## Jinja2, Boostrap and Crispy Forms

For nicer and quicker development with forms, there is the branch jinja2_bootstrap4

This gives you a basic responsive layout with a menu-bar that you can build upon.

To use crispy forms, just write the tag `{{ crispy(form) }}` in your template, at the posititon where you want the form to appear.

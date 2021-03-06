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

To use this for your own projects run `setup.py`. This will ask you for new project and application
names, and then make all the changes needed in the files. It will also generate a new secret key
for your project. `setup.py` assumes the project is still a git-repo and it will create a new branch
by the name of your project as well.

To do this manually, just replace the string `myapp` all over the project with your application name.
Also replace the string `djproject` all over the code with your project name.
It is safe to do this via a script, if you rename only lowercase strings or can preserve the case (like in PyCharm). Only the class MyAppConfig has camel-case, but you can leave that also as it is.

Renaming will also change the name of the containers, databases, database, the volume and the network, so there will be no conflicts between parallel projects. You only have to change the port mapping manually in `docker-compose.yml`, if you want to run stuff in parallel.

## Jinja2, Boostrap and Crispy Forms

For nicer and quicker development with forms, there is the branch jinja2_bootstrap4

This gives you a basic responsive layout with a menu-bar that you can build upon.

To use crispy forms, just write the tag `{{ crispy(form) }}` in your template, at the posititon where you want the form to appear.

## License

This code is provided under GNU General Public License v3.0

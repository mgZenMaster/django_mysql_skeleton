#!/usr/bin/env python3

import os
import pathlib
import re


def re_upper(match):
    return match.group(1).upper()


def replace_in_file(search, replace, file):
    with open(file, "rt") as f:
        contents = f.read()
    contents = contents.replace(search, replace)

    with open(file, "wt") as f:
        f.write(contents)


base_path = pathlib.Path(__file__).parent.absolute()

project_name = input("Your project name:")
project_name_lower = project_name.lower().replace(" ", "")
application_name = input("Your application name:")
application_name_lower = application_name.lower().replace(" ", "")
application_name_camel = re.sub(r'(?:^| |_|-)+([a-zA-Z])', re_upper, application_name_lower)

os.system(f'git checkout -b {project_name_lower} ')

replace_in_file('djproject', project_name_lower,
                os.path.join(base_path, 'djproject', 'settings.py'))

replace_in_file('djproject', project_name_lower,
                os.path.join(base_path, 'djproject', 'urls.py'))

replace_in_file('djproject', project_name_lower,
                os.path.join(base_path, 'djproject', 'wsgi.py'))

replace_in_file('myapp', application_name_lower,
                os.path.join(base_path, 'docker-compose.yml'))

replace_in_file('myapp', application_name_lower,
                os.path.join(base_path, 'docker-entrypoint.sh'))

replace_in_file('myapp', application_name_lower,
                os.path.join(base_path, 'waitfordb.py'))

replace_in_file('myapp.apps.MyAppConfig', f'{application_name_lower}.apps.{application_name_camel}Config',
                os.path.join(base_path, 'djproject', 'settings.py'))

replace_in_file('MyAppConfig', f'{application_name_camel}Config',
                os.path.join(base_path, 'myapp', 'apps.py'))

replace_in_file('myapp', application_name_lower,
                os.path.join(base_path, 'djproject', 'settings.py'))

os.system(f'git mv myapp {application_name_lower}')
os.system(f'git mv djproject {project_name_lower}')

import re
import sys


slug = '{{ cookiecutter.project_slug }}'
node_version = '{{ cookiecutter.node_version }}'


if not re.match(r'^[a-z0-9-]+$', slug):
    sys.stderr.write('project_slug must be lowercase letters, numbers, and dashes\n')
    sys.exit(1)


if not re.match(r'^\d+$', node_version):
    sys.stderr.write('node_version must be a major version number, e.g. 22\n')
    sys.exit(1)
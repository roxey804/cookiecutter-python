import os

# Remove files if not using python
{%- if cookiecutter.language != "python" -%}
python_files = [
    os.path.join('{{cookiecutter.project_name}}','setup.py'),
    os.path.join('{{cookiecutter.project_name}}', 'tests', 'conftest.py')

]

for file in python_files:
    os.remove(file)

{% endif %}

# Remove files if not using node_js
{%- if cookiecutter.language != "node_js" -%}
node_js_files = [
]

for file in node_js_files:
    os.remove(file)

{% endif %}

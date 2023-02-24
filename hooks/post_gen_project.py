import os

language = '{{cookiecutter.language}}'
python_files = [
    'setup.py',
    os.path.join('../{{cookiecutter.project_name}}', 'tests', 'conftest.py')

]
node_js_files = [
]

# Remove files if not using python
if language != "python":
    for file in python_files:
        os.remove(file)

# Remove files if not using node_js
if language != "node_js":
    for file in node_js_files:
        os.remove(file)

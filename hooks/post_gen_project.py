import os


language = '{{cookiecutter.language}}'
generate_reqs = {{cookiecutter.generate_requirements}}
python_files = [
    'setup.py',
    create_reqs(),
    os.path.join('tests', 'conftest.py')
]

node_js_files = [
    'package.json'
]

def create_reqs():
    if generate_reqs == "y":
        file = open("requirements.txt", 'a').close()
    return file

# Remove files if not using python
if language != "python":
    for file in python_files:
        os.remove(file)

# Remove files if not using node_js
if language != "node_js":
    for file in node_js_files:
        os.remove(file)

### Prevent Make commands outside a virtualenv or conda env
venv:
ifndef VIRTUAL_ENV
ifndef CONDA_PREFIX
$(error VIRTUAL / CONDA ENV is not set - please activate environment)
endif
endif

### Make commands ###
deps: venv
  @echo "Installing Dependencies"
  {% if cookiecutter.language == 'python'}	pip install --upgrade pip
  pip install . {% endif %}
  {% if cookiecutter.language == 'node_js'} npm install {% endif %}

clean: venv
	@echo "Removing build artifacts / temp files"
	{% if cookiecutter.language == 'python'}	find . -name "*.pyc" -delete {% endif %}
	{% if cookiecutter.language == 'node_js'}	rm -rf node_modules
 	npm cache verify {% endif %}

test: clean
	@echo "Running tests"
	pytest tests/

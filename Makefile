#################################################################################
# COMMANDS                                                                      #
#################################################################################
GUNICORN_WORKERS = 1
GUNICORN_PORT = 8000
GUNICORN_TIME_OUT = 60

format:
	set -e
	isort --recursive  --force-single-line-imports app tests
	autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place app tests
	black app tests
	isort --recursive app tests

lint:
	set -e
	set -x
	flake8 app --exclude=app/core/config.py
	black --check --diff app 
	isort --recursive --check-only app


install_req:
	@echo "Installing requirements...."
	pip install -r requirements.txt

.clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

run_dev_server:
	uvicorn app.main:app --host 0.0.0.0 --port 8002 --reload


run_server:
	gunicorn --bind 0.0.0.0:${GUNICORN_PORT} app.main:app --workers ${GUNICORN_WORKERS} --timeout ${GUNICORN_TIME_OUT} -k uvicorn.workers.UvicornWorker

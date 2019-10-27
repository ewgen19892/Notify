.PHONY: all fixtures static locale

all: test lint

test:
	mkdir -p reports
	coverage run manage.py test ${APP}
	coverage report -m --skip-covered
	coverage xml -i -o reports/coverage.xml
	sed -i 's_/app_src_g' /app/reports/coverage.xml
	chmod -R 777 reports/

lint:
	mkdir -p reports
	flake8 ${APP}
	isort -y --recursive ${APP}
	chmod -R 777 reports/

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	isort -y --recursive ${APP}
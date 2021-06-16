install:
	poetry install

uninstall:
	pip uninstall hexlet-code

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl


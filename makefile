build:
	python setup.py sdist
	python setup.py bdist_wheel

clean:
	pyclean .
	if exist .\src\databurglar\.mypy_cache rmdir .\src\databurglar\.mypy_cache /q /s
	if exist .\build rmdir .\build /q /s
	if exist .\dist rmdir .\dist /q /s
	if exist .\src\databurglar.egg-info rmdir .\src\databurglar.egg-info /q /s

mypy:
	cd ./src/databurglar && mypy ./ --ignore-missing-imports

run-integrations:
	python ./integrations/db_test.py

upload:
	twine upload dist/*

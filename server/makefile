RM = rm -rf

clean:
	find . -name "__pycache__" -type d -exec $(RM) -r {} +
	find . -name "*.pyc" -type f -exec $(RM) {} +
	$(RM) -rf .pytest_cache

test:
	COODIE_MODE=testing pytest -vv -W ignore::DeprecationWarning

dev:
	cd src && COODIE_MODE=development uvicorn app:app --reload

code-convention:
	poetry run flake8
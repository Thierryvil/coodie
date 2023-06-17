RM = rm -rf

clean:
	find . -name "__pycache__" -type d -exec $(RM) -r {} +
	find . -name "*.pyc" -type f -exec $(RM) {} +
	$(RM) -rf .pytest_cache
	$(RM) -f coverage .coverage

test:
	COODIE_MODE=testing pytest -vv --cov=. --cov-report=html --cov-report=term -W ignore::DeprecationWarning

dev:
	cd src && COODIE_MODE=development uvicorn app:app --reload

code-convention:
	flake8
	pycodestyle
RM = rm -rf

clean:
	find . -name "__pycache__" -type d -exec $(RM) -r {} +
	find . -name "*.pyc" -type f -exec $(RM) {} +
	$(RM) -rf .pytest_cache

test:
	export ENV_FOR_DYNACONF=testing && pytest -vv -W ignore::DeprecationWarning

dev:
	export ENV_FOR_DYNACONF=development && uvicorn src.app:app --reload
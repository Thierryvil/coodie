RM = rm -rf

ifdef WSL_DISTRO_NAME
	PYCLEAN = find . -name "__pycache__" -type d -exec $(RM) -r {} +
	PYCLEAN += find . -name "*.pyc" -type f -exec $(RM) {} +
	PYCLEAN += $(RM) -rf .pytest_cache
	PYTEST = export ENV_FOR_DYNACONF=testing && pytest -vv
else
	PYCLEAN = python -c "import glob, os; [os.remove(f) for f in glob.glob('**/*.pyc', recursive=True)]; [os.rmdir(d) for d in glob.glob('**/__pycache__', recursive=True)]; import shutil; shutil.rmtree('.pytest_cache', ignore_errors=True)"
	PYTEST = set ENV_FOR_DYNACONF=testing && pytest -vv
endif

clean:
	$(PYCLEAN)

test:
	$(PYTEST)

dev:
	uvicorn src.app:app --reload
# Makefile

install:
	pip install -r requirements.txt

run:
	python -m loopa

test:
	pytest pytest_loopa/

clean:
	rm -rf __pycache__ pytest_loopa/__pycache__ loopa/__pycache__

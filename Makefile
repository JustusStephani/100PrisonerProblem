VENV := venv

install: requirements.txt
	python3.7 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip3 install -r requirements.txt

test:
	PYTHONPATH=. ./$(VENV)/bin/pytest

clean:
	./$(VENV)/bin/python3 -m black main.py
	./$(VENV)/bin/python3 -m black src/prisionExperiment.py

.PHONY: install clean
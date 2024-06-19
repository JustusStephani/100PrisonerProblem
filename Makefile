VENV := venv

install: requirements.txt
	python3.7 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip3 install -r requirements.txt

clean:
	./$(VENV)/bin/python3 -m black src/main.py

.PHONY: install clean
run-web-server:
	PYTHONPATH="$$PWD:$$PYTHONPATH" fastapi dev --port 2001 src/web/app.py
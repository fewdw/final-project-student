web: cd flask-api && gunicorn app:app --bind 0.0.0.0:$PORT --timeout 90
worker: cd flask-frontend && gunicorn app:app --bind 0.0.0.0:$PORT --timeout 90

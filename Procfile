# web: gunicorn -b 0.0.0.0:$PORT 'web:create_app()' --preload
web: gunicorn -b 0.0.0.0:$PORT --chdir .web '__init__:create_app()' --preload --timeout 10 --max-requests 50

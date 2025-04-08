# gunicorn.conf.py

bind = "0.0.0.0:8000"  # <-- This allows access from outside the container
workers = 2
worker_class = "gthread"
threads = 4
timeout = 120

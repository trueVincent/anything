import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
timeout = 30
max_requests = 1000
backlog = 2048
debug = False
logLevel = "debug"
accesslog = "./logs/gunicorn_access.log"
errorlog = "./logs/gunicorn_error.log"

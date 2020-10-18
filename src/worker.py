from redis import Redis
from rq import Queue, Worker
from datetime import datetime
from web_hook_job import handle_job
import moment
import os

redis_host = os.environ.get('REDIS_HOST') or 'localhost'
redis_port = os.environ.get('REDIS_PORT') or 6379

redis = Redis(host=redis_host, port=redis_port)
queue = Queue(connection=redis)
worker = Worker([queue], connection=redis)

def start_worker():
    worker.work(with_scheduler=True)

def set_job(params):
    # job = queue.enqueue_at(datetime(2020, 10, 13, 22, 36), handle_event)
    queue.enqueue_at(moment.date(params["time"]).date, handle_job, params, job_id=params["id"])

def list_scheduled_jobs():
    return queue.scheduled_job_registry.get_job_ids()

def list_failed_jobs():
    return queue.failed_job_registry.get_job_ids()

def delete_job(id):
    return queue.scheduled_job_registry.remove(id)

def get_job(id):
    return queue.scheduled_job_registry.get_queue().fetch_job(id)

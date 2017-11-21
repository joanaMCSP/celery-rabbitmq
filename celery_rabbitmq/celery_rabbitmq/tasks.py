from functools import wraps
from celery_rabbitmq.celeryconf import app
from .models import Job
from bs4 import BeautifulSoup
import requests
import json

def update_job(fn):
    @wraps(fn)
    def wrapper(job_id, *args, **kwargs):
        job = Job.objects.get(id=job_id)
        job.status = 'started'
        job.save()
        try:
            job.result = fn(*args, **kwargs)
            job.status = 'finished'
            job.save()
        except Exception as e:
            job.result = "The task could not be processed.Check your input"
            job.status = 'failed'
            job.save()
    return wrapper

@app.task
@update_job
def map_url(s):
    """Takes a url as a string and returns a word count dictionary"""
    c = {}
    r = requests.get(s)
    soup = BeautifulSoup(r.text)
    for script in soup(["script", "style"]):
        script.extract()
    for word in soup.get_text().split():
        word.strip()
        if word not in c:
            c[word] = 0
        c[word] += 1
    return c

@app.task
@update_job
def merge_maps(s):
    """Takes a list of word count dictionaries as a json string
    and returns a single merged dictionary """
    merged = {}
    map_list = json.loads(s)
    for d in map_list:
        for key, value in d.items():
            merged[key] = value
    return merged

TASK_MAPPING = {
    'map_url': map_url,
    'merge_maps': merge_maps
}

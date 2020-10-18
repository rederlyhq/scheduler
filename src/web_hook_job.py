import requests
import json

def handle_job(params):
    resp = requests.post(params['webHookScheduleEvent']['url'], data=params['webHookScheduleEvent']['data'])
    if resp.status_code < 200 or resp.status_code > 299:
        raise Exception(f'Request failed with status code: {resp.status_code}; Params: {json.dumps(params)}; Response: {resp.text}')
    print(resp.text)

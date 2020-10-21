import requests
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_job(params):
    resp = requests.post(params['webHookScheduleEvent']['url'], data=params['webHookScheduleEvent']['data'])
    if resp.status_code < 200 or resp.status_code > 299:
        error = f'Request failed with status code: {resp.status_code}; Params: {json.dumps(params)}; Response: {resp.text}'
        logger.error(json.dumps({'msg': error}))
        raise Exception(error) # not needed ?
    else:
        logger.info(json.dumps({"msg": "backend call back", 'data': json.dumps(params['webHookScheduleEvent']['data'])}))



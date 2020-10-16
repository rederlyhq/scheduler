import requests

def handle_job(params):
    try:
        resp = requests.post(params['webHookScheduleEvent']['url'], data=params['webHookScheduleEvent']['data'])
        print(resp)
    except Exception as inst:
        print('An error has occurred executing the web hook handle event: ' + str(inst))

#!/usr/bin/python3
from server import start_server
from worker import start_worker
import threading
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info(json.dumps({"msg" : "Proccess Starting"}))

# Thread must be daemon so that it quits with the application
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# # Using main thread due to error
# # `ValueError: signal only works in main thread`
# worker_thread = threading.Thread(target=start_worker)
# worker_thread.start()
start_worker()

logger.info(json.dumps({"msg": "Proccess Ending"}))
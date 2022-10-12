import json
import logging

import azure.functions as func

def main(request):
    logging.info(request)
    logging.info(json.loads(request)["connectionContext"]["userId"])
    logging.info('Python HTTP trigger function processed a request.')
    
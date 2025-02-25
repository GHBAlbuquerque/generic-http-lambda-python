import json
import logging
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from src.client.http_client import HttpClient

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_request(event, context):
    correlation_id=event.get('correlation_id')
    timeout=event.get('timeout', 10) # default 10 seconds
    retry_attempts=event.get('retry_attempts', 3) # default 3 attempts

    logger.info(f"Handling request with correlation_id: {correlation_id}")

    # Create a requests session with retries and timeout
    requestSession = requests.Session()
    retries = Retry(total=retry_attempts, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    requestSession.mount('http://', HTTPAdapter(max_retries=retries))
    requestSession.options(timeout=timeout)

    # Create an HttpClient instance
    client = HttpClient(requestSession)

    try: 
        response = client.handle_request(event.get('method'), 
                                         event.get('url'), 
                                         event.get('headers'), 
                                         event.get('body')
                                         )

        logger.info(f"Response: {response}")
        logger.info(f"Response handled sucessfully. Response status code: {response.get('status_code')}")

        return response

    except requests.Exception as e:
        logger.error("An error occurred while handling request", exc_info=True)
        
        return {
            'statusCode': e.response.status_code,
            'body': e.response.text
        }
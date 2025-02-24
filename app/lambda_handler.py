import json
import logging
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_request(event, context):
    correlation_id=event.get('correlation_id')
    timeout=event.get('timeout', 10) # default 10 seconds
    retry_attempts=event.get('retry_attempts', 3) # default 3 attempts

    logger.info(f"Handling request with correlation_id: {correlation_id}")

    # Create a session with retries
    session = requests.Session()
    retries = Retry(total=retry_attempts, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))

    
import requests
import logging
from typing import Dict, Any, Optional

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

class HttpClient:
    def __init__(self, session : requests.Session):
        self.session = session

    def handle_request(self, 
                       method : str,
                       url: str,
                       headers: Optional[Dict[str, Any]] = Any,
                       body: Optional[str] = None) -> Dict[str, Any]:
        
        logger.info("Handling request")

        try:
            response = self.session.request(method=method,
                                            url=url,
                                            headers=headers,
                                            json=body)
            response.raise_for_status() #raises a HTTPError if the HTTP request returned an unsuccessful status code

            parsed_body=self.parse_body(response)
            parsed_headers=self.parse_headers(response.headers)

            return {
                "status_code": response.status_code,
                "body": parsed_body,
                "headers": parsed_headers
            }

        except requests.Exception as e:
            logger.error("An error occurred while handling request", exc_info=True)
            raise e
        
    def parse_headers(self, headers: requests.structures.CaseInsensitiveDict) -> Dict[str, str]: 
        return dict(headers)
    
    def parse_body(self, response: requests.Response) -> Any:
        try:
            return response.json()
        except ValueError:
            return response.text
from typing import Optional, Dict, Any

class RequestInput:
    def __init__(self,
                 url: str,
                 method: str,
                 timeout: int,
                 retry_attempts: int,
                 headers: Optional[Dict[str, Any]] = None,
                 body: Optional[str] = None,
                 correlation_id: str = ''):
        
        self.url = url
        self.method = method
        self.timeout = timeout
        self.retry_attempts = retry_attempts
        self.headers = headers
        self.body = body
        self.correlation_id = correlation_id
        
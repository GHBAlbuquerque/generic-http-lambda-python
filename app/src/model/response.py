from typing import Optional, Dict

class Response:
    def __init__(self,
                 status_code: int,
                 headers: Optional[Dict[str,str]] = None,
                 body: Optional[str] = None):
        self.status_code = status_code
        self.headers = headers
        self.body = body


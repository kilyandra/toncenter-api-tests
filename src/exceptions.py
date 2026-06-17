class APIRequestError(Exception):
    def __init__(self, status_code, api_code, message):
        self.status_code = status_code
        self.api_code = api_code
        self.message = message
        super().__init__(message)

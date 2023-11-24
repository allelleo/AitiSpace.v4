import httpx

from app.config import SpaceLog_host, SpaceLog_service, SpaceLog_project
from app.wrappers import ignore_error


class SpaceLogClient:
    def __init__(self, host):
        self.host = host
        self.client = httpx.Client()
        self.timeout = 0.000001
        self.project = SpaceLog_project
        self.service = SpaceLog_service

    @ignore_error
    def CRITICAL(self, message: str = "Critical Error", code: int = 0, level='CRITICAL'):
        self.client.post(f"{self.host}/api/v1/log", json={
            'project': self.project,
            'service': self.service,
            'level': level,
            'message': message,
            'code': code
        }, timeout=self.timeout)

    @ignore_error
    def WARNING(self, message: str = "Warning Error", code: int = 0, level='Warning'):
        self.client.post(f"{self.host}/api/v1/log", json={
            'project': self.project,
            'service': self.service,
            'level': level,
            'message': message,
            'code': code
        }, timeout=self.timeout)

    @ignore_error
    def INFO(self, message: str = "Info Error", code: int = 0, level='INFO'):
        self.client.post(f"{self.host}/api/v1/log", json={
            'project': self.project,
            'service': self.service,
            'level': level,
            'message': message,
            'code': code
        }, timeout=self.timeout)

    @staticmethod
    def get_logger():
        return SpaceLogClient(SpaceLog_host)


logger = SpaceLogClient.get_logger()
get_logger = SpaceLogClient.get_logger

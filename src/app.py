from src.config.settings import settings
from src.domain.service import GreetingService


def main():
    service = GreetingService()
    message = service.greet(settings.app_name)
    print(message)

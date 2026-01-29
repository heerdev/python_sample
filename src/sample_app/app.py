from sample_app.config.settings import settings
from sample_app.domain.service import GreetingService


def main():
    service = GreetingService()
    message = service.greet(settings.app_name)
    print(message)

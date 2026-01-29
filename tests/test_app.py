from src.domain.service import GreetingService


def test_greet():
    service = GreetingService()
    assert service.greet("TestApp") == "Hello from TestApp 👋"

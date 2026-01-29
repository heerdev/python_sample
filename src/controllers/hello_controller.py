from fastapi import APIRouter, Depends
from src.domain.service import GreetingService

router = APIRouter()

def get_greeting_service():
  return GreetingService()

@router.get("/hello")
def hello(service: GreetingService = Depends(get_greeting_service)):
    return {"message": service.greet("Alice")}
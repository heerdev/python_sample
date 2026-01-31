from fastapi import APIRouter, Depends
import matplotlib.pyplot as plt
import networkx as nx
from src.domain.service import GreetingService

router = APIRouter()

def get_greeting_service():
  return GreetingService()

@router.get("/hello")
def hello(service: GreetingService = Depends(get_greeting_service)):
      G = nx.Graph()
      G.add_edges_from([(1,2),(2,3),(3,1)])
      nx.draw(G, with_labels=True)
      plt.show()
      return {"message": service.greet("Alice")}

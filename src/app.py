from fastapi import FastAPI
from .controllers.hello_controller import router as hello_router

app = FastAPI(title="Sample Python App")
app.include_router(hello_router)


def main():
	import uvicorn
	uvicorn.run(app, host="127.0.0.1", port=8000)
from fastapi import FastAPI

from app.controllers import book_controller

app = FastAPI()

app.include_router(book_controller.router)


@app.get("")
def get_test():
    print("doing nothing")
    return {"message": "hello"}

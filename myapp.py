import uvicorn
from fastapi import FastAPI

app = FastAPI()
origins = [
    "*"
]

@app.get("/")
def say_hi():
    return { my_name() }

def my_name():
    return "Mi nombre es Alexis"

if __name__=='__main__':
     uvicorn.run(app, host="0.0.0.0", port=8000)
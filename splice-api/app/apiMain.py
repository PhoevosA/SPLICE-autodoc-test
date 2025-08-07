from fastapi import FastAPI
from splice_lib import main

app = FastAPI()


def get_random_number():
    return { "random": main.random_number() }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host= "0.0.0.0", port = 8000)

from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def health():
    return {"status": "healthy"}

@app.get("/orders")
def orders_stable():
    time.sleep(0.05)
    return {"orders": 10}

@app.get("/orders-buggy")
def orders_buggy():
    total = 0
    for i in range(3 * 10**7):   # Safe for t3.micro
        total += i
    return {"orders": total}

@app.get("/orders-recovered")
def orders_recovered():
    time.sleep(0.05)
    return {"orders": 10}
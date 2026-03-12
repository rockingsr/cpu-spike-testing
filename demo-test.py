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
    # FIX: Replaced CPU-intensive loop with a deterministic constant to prevent compute drift in high-load scenarios.
    # The previous loop iterated 3*10**7 times, consuming significant CPU and causing inefficiency described in RCA.
    total = 10
    return {"orders": total}

@app.get("/orders-recovered")
def orders_recovered():
    time.sleep(0.05)
    return {"orders": 10}

from fastapi import FastAPI
import time
import os

app = FastAPI()

@app.get("/")
def health():
    return {"status": "healthy"}

@app.get("/orders")
def orders_stable():
    # Lightweight endpoint to simulate a normal workload
    time.sleep(0.05)
    return {"orders": 10}

# /orders-buggy endpoint:
# Intent: mirror the original heavy CPU path for testing.
# Risk: without safeguards, could cause CPU spike under load.
# Mitigation: gate this path by default. It only runs the heavy loop if explicitly enabled via
# a query parameter or environment variable set to true.
@app.get("/orders-buggy")
def orders_buggy(enable: str = None):
    allow = os.environ.get("ALLOW_BUGGY", "false").lower()
    if (enable == "true") or (allow == "true"):
        total = 0
        for i in range(3 * 10**7):
            total += i
        return {"orders": total}
    else:
        return {"error": "orders-buggy is disabled in this environment"}

@app.get("/orders-recovered")
def orders_recovered():
    # Lightweight recovery path after a simulated load
    time.sleep(0.05)
    return {"orders": 10}
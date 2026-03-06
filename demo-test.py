from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def health():
    return {"status": "healthy"}

# FIX: Gate heavy computation to prevent CPU spike by using a gating flag (query parameter 'gate').
@app.get("/orders")
def orders_stable():
    time.sleep(0.05)
    return {"orders": 10}

# FIX: Gate heavy computation to prevent CPU spike by using a gating flag (query parameter 'gate').
@app.get("/orders-buggy")
def orders_buggy(gate: bool = False):
    # FIX: If gating is not enabled, return quickly to avoid CPU spike.
    if not gate:
        return {"orders": 0}
    # FIX: Heavy loop is now guarded by the 'gate' flag to restore RCA gating behavior.
    total = 0
    for i in range(3 * 10**7):   # Heavy computation gated behind 'gate'
        total += i
    return {"orders": total}

@app.get("/orders-recovered")
def orders_recovered():
    time.sleep(0.05)
    return {"orders": 10}

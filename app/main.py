import os
import shutil
import socket
import time

from fastapi import FastAPI

app = FastAPI(title="System Status API")

START_TIME = time.time()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/status")
def status():
    disk = shutil.disk_usage("/")
    return {
        "hostname": socket.gethostname(),
        "uptime_seconds": round(time.time() - START_TIME),
        "disk_total_gb": round(disk.total / 1e9, 2),
        "disk_free_gb": round(disk.free / 1e9, 2),
        "environment": os.getenv("APP_ENV", "development"),
    }

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import os

from database import get_db_connection, create_table
from geo import get_geo_info

app = FastAPI()
templates = Jinja2Templates(directory="templates")

ADMIN_PASSWORD = "maxfiyparol"  # Ertaga .env faylga chiqarish mumkin

create_table()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    ip = request.client.host
    port = str(request.client.port)
    method = request.method
    path = request.url.path
    geo = get_geo_info(ip)
    timestamp = datetime.utcnow().isoformat()

    conn = get_db_connection()
    conn.execute(
        '''INSERT INTO logs (ip, port, method, path, country, region, city, timestamp)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (ip, port, method, path, geo['country'], geo['region'], geo['city'], timestamp)
    )
    conn.commit()
    conn.close()
    return response

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("unauthorized.html", {"request": request})

@app.get("/logs", response_class=HTMLResponse)
async def show_logs(request: Request, password: str = ""):
    if password != ADMIN_PASSWORD:
        return RedirectResponse("/")
    conn = get_db_connection()
    logs = conn.execute("SELECT * FROM logs ORDER BY id DESC").fetchall()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "logs": logs})

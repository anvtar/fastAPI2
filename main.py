import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from datetime import datetime
from public.router_users import users_router, goods_router

app = FastAPI()

app.include_router(users_router)
app.include_router(goods_router)
@app.on_event("startup")
def on_startup():
    open("log_p.txt", mode="a").write(f'{datetime.utcnow()}: Begin\n')

@app.on_event("shutdown")
def shutdown():
    open("log_p.txt", mode="a").write(f'{datetime.utcnow()}: End\n')

@app.get("/")
def main():
    return FileResponse("files/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sockets import sio_app,sio_server

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/raise-appointment")
async def test():
    return await sio_server.emit('new-appointment', {
        "name":"ra kumar",
        "issue":"Fever",
        "date":"2024-12-07"
    })

app.mount('/', sio_app)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
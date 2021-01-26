import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.Routes.router import api_router
app=FastAPI()
app.include_router(api_router, prefix="/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80, debug=True)
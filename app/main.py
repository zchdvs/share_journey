from fastapi import FastAPI
from routers import discord, midjourney

app = FastAPI()

app.include_router(discord.router)
app.include_router(midjourney.router)

import uvicorn

if __name__ == "__main__":
  uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)
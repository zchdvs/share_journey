from fastapi import FastAPI
from routers import discord, midjourney
import uvicorn
app = FastAPI()

app.include_router(discord.router)
app.include_router(midjourney.router)

@app.get("/")
async def test():
  return 'asdf'
if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=80, reload=True)
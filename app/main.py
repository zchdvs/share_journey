from fastapi import FastAPI
from routers import discord, midjourney

app = FastAPI()

app.include_router(discord.router)
app.include_router(midjourney.router)

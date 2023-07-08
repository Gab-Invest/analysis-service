"""Provides the necessary methods to bootstrap a server"""
from fastapi import FastAPI
from src.routes import router


app = FastAPI(routes=router.routes)

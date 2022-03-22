
from pymongo import MongoClient
from app.core.config import settings

conn = MongoClient(settings.DATABASE_URL)
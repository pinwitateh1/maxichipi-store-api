import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "Maxichipi store api"
    PROJECT_VERSION: str = "1.0.0"

    MONGO_USER : str = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_SERVER : str = os.getenv("MONGO_SERVER","localhost")
    #MONGO_PORT : str = os.getenv("MONGO_PORT",5432) # default postgres port is 5432
    MONGO_DB : str = os.getenv("MONGO_DB") # default postgres port is 5432
    DATABASE_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_SERVER}/{MONGO_DB}"

settings = Settings()
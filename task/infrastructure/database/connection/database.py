from sqlalchemy import MetaData, create_engine

from config import Config

engine = create_engine(Config.DATABASE_URL, echo=True)
metadata = MetaData()

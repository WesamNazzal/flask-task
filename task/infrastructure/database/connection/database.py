from sqlalchemy import create_engine, MetaData
from config import Config

engine = create_engine(Config.DATABASE_URL, echo=True)
metadata = MetaData()
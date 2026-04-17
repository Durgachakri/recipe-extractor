from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:Chakri%40sql_1@localhost/recipe_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
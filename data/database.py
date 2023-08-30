from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data.model import InsectTable, SpiderTable
from Insects import insects
from spiders import Spiders

DATABASE_URL = "sqlite:///insect_dict.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(engine)

def populate_database(insects, spiders):
    session = SessionLocal()
    
    for insect_data in insects:
        insect = InsectTable(
            name=insect_data.name,
            scientific_name=insect_data.scientific_name,
            habitat=insect_data.habitat,
            diet=insect_data.diet,
            behavior=insect_data.behavior
        )
        session.add(insect)

    for spider_data in spiders:
        spider = SpiderTable(
            name=spider_data.name,
            scientific_name=spider_data.scientific_name,
            habitat=spider_data.habitat,
            diet=spider_data.diet,
            behavior=spider_data.behavior,
            venomous=spider_data.venomous
        )
        session.add(spider)

    session.commit()
    session.close()

def initialize_database():
    Base.metadata.drop_all(engine)
    create_tables()
    populate_database(insects, Spiders)

if __name__ == "__main__":
    initialize_database()

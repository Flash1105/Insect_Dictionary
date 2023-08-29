from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.model import Base, InsectTable, SpiderTable, AnimalFact
from Insects import insects
from spiders import Spiders

# Database setup
DATABASE_URL = 'sqlite:///insect_database.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
def create_tables():
    Base.metadata.create_all(engine)

# Populate the database
def populate_database(insects, spiders):
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



def initialize_database(session):
    Base.metadata.drop_all(engine)
    create_tables()
    populate_database(insects, Spiders)

if __name__ == "__main__":
    initialize_database()
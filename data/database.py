from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///insect_dict.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    from data.model import Base
    Base.metadata.create_all(engine)

def populate_database(insects, spiders):
    from data.model import InsectTable, SpiderTable
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
    from data.model import Base
    Base.metadata.drop_all(engine)
    create_tables()
    
    from Insects import insects
    from spiders import Spiders
    populate_database(insects, Spiders)

if __name__ == "__main__":
    initialize_database()

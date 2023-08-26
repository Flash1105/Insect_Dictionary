from Insects import insects, Insect
from spiders import spiders, Spider
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.model import Base, Insect, Spider

# Database setup
DATABASE_URL = 'sqlite:///insect_database.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# create tables
def create_tables():
    Base.metadata.create_all(engine)

# populate the database
def populate_database(insects, spiders):
    for insect_data in insects:
        insect = Insect(**insect_data)
        session.add(insect)

    for spider_data in spiders:
        spider = Spider(**spider_data)
        session.add(spider)

    session.commit()

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from Insects import insects, Insect
from spiders import spiders, Spider

# creates database with SQlite
engine = create_engine('sqlite:///insect_database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class InsectTable(Base):
    __tablename__ = 'insects'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)

class SpiderTable(Base):
    __tablename__ = 'spiders'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)
    venomous = Column(Boolean)

# make tables in database
Base.metadata.create_all(engine)

# populate the database
def populate_database():
    for insect_data in insects:
        insect = InsectTable(**insect_data.__dict__)
        session.add(insect)
    for spider_data in spiders:
        spider = SpiderTable(**spider_data.__dict__)
        session.add(spider)
    session.commit()


# Home page
def display_home_page():
    print("Welcome to the Insect and Spider Encyclopedia!")
    print("Available Insects and Spiders:")
    for index, insect in enumerate(insects + spiders, start=1):
        print(f"{index}. {insect['name']}")
    print()

if __name__ == "__main__":
    populate_database()
    display_home_page()

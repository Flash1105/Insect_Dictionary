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
        existing_insect = session.query(InsectTable).filter_by(name=insect_data['name']).first()
        if not existing_insect:
            insect = InsectTable(**insect_data.__dict__)
            session.add(insect)
    
    for spider_data in spiders:
        existing_spider = session.query(SpiderTable).filter_by(name=spider_data['name']).first()
        if not existing_spider:
            spider = SpiderTable(**spider_data.__dict__)
            session.add(spider)
    session.commit()


# Home page
def display_home_page():
    print("Welcome to the Insect and Spider Encyclopedia!")
    print("Available Insects and Spiders:")
    for index, animal in enumerate(insects + spiders, start=1):
        print(f"{index}. {animal.name}")
    print()

    try:
        selection = int(input("Enter the number of the animal to get more information: "))
        selected_animal = (insects + spiders)[selection - 1]
        print("\nAnimal Information:")
        print(f"Name: {selected_animal.name}")
        print(f"Scientific Name: {selected_animal.scientific_name}")
        print(f"Habitat: {selected_animal.habitat}")
        print(f"Diet: {selected_animal.diet}")
        print(f"Behavior: {selected_animal.behavior}")
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid number.")

if __name__ == "__main__":
    populate_database()
    display_home_page()

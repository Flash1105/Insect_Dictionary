from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from data.database import DATABASE_URL
from data.model import InsectTable, SpiderTable

#setup for database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def display_insect_details(animal):
    print("\nSelected Insect:")
    print(f"Name: {animal.name}")
    print(f"Scientific Name: {animal.scientific_name}")
    print(f"Habitat: {animal.habitat}")
    print(f"Diet: {animal.diet}")
    print(f"Behavior: {animal.behavior}")
    if isinstance(animal, SpiderTable):
        print(f"Venomous: {'Yes' if animal.venomous else 'No'}")

def display_animal_list():
    print("Available Animals:")
    insects = session.query(InsectTable).all()
    spiders = session.query(SpiderTable).all()
    
    for index, animal in enumerate(insects + spiders, start=1):
        print(f"{index}. {animal.name}")
    print()

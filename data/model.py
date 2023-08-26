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
        existing_insect = session.query(InsectTable).filter_by(name=insect_data.name).first()
        if not existing_insect:
            insect = InsectTable(
                name=insect_data.name,
                scientific_name=insect_data.scientific_name,
                habitat=insect_data.habitat,
                diet=insect_data.diet,
                behavior=insect_data.behavior
            )
            session.add(insect)

    for spider_data in spiders:
        existing_spider = session.query(SpiderTable).filter_by(name=spider_data.name).first()
        if not existing_spider:
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

# display list of insects
def display_animal_list():
    print("Available Insects:")
    for index, animal in enumerate(insects, start=1):
        print(f"{index}. {animal.name}")
    print()

# Display spider list

def display_spider_list():
    print("Available Spiders:")
    for index, spider in enumerate(spiders, start=1):
        print(f"{index}. {spider.name}")
    print()

# display details of animal
def display_animal_details(animal):
    print("\nAnimal Information:")
    print(f"Name: {animal.name}")
    print(f"Scientific Name: {animal.scientific_name}")
    print(f"Habitat: {animal.habitat}")
    print(f"Diet: {animal.diet}")
    print(f"Behavior: {animal.behavior}")
    if isinstance(animal, Spider):
        print(f"Venomous: {'Yes' if animal.venomous else 'No'}")


# Home page

def homepage():
    print("Welcome to the Insect and Spider Encyclopedia!")
    print("1. Get an insect fact")
    print("2. Get a spider fact")
    print("3. Exit")

def main_menu():
    while True:
        homepage()

        choice = input("Enter your choice: ")

        if choice == "1":
            display_animal_list()
            animal_index = int(input("Enter the number of the animal: "))
            if 1 <= animal_index <= len(insects + spiders):
                selected_animal = (insects + spiders)[animal_index - 1]
                display_animal_details(selected_animal)
            else:
                print("Invalid animal number.")
        elif choice == "2":
            display_spider_list()
            spider_index = int(input("Enter the number of the spider: "))
            if 1 <= spider_index <= len(spiders):
                selected_spider = spiders[spider_index - 1]
                display_animal_details(selected_spider)
            else:
                print("Invalid spider number.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
        

if __name__ == "__main__":
    populate_database()
    main_menu()
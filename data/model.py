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


# Home page

def homepage():
    print("Welcome to the Insect and Spider Encyclopedia!")
    print("1. Get a spider fact")
    print("2. Get an insect fact")
    print("3. Exit")

def main_menu():
    while True:
        homepage()

        choice = input("Enter your choice: ")

        if choice == "1":
            spider_name = input("Enter the name of the spider: ")
            display_spider_details(spider_name)
        elif choice == "2":
            insect_name = input("Enter the name of the insect: ")
            display_insect_details(insect_name)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def display_spider_details(name):
    spider = session.query(SpiderTable).filter_by(name=name).first()
    if spider:
        print("Spider Information:")
        print(f"Name: {spider.name}")
        print(f"Scientific Name: {spider.scientific_name}")
        print(f"Habitat: {spider.habitat}")
        print(f"Diet: {spider.diet}")
        print(f"Behavior: {spider.behavior}")
        print(f"Venomous: {spider.venomous}")
    else:
        print("Spider not found.")

def display_insect_details(name):
    insect = session.query(InsectTable).filter_by(name=name).first()
    if insect:
        print("Insect Information:")
        print(f"Name: {insect.name}")
        print(f"Scientific Name: {insect.scientific_name}")
        print(f"Habitat: {insect.habitat}")
        print(f"Diet: {insect.diet}")
        print(f"Behavior: {insect.behavior}")
    else:
        print("Insect not found.")

if __name__ == "__main__":
    populate_database()
    main_menu()
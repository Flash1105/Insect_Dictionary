from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from data.database import DATABASE_URL
from data.model import InsectTable, SpiderTable

#setup for database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    while True:
        print("Welcome to the Insect and Spider Encyclodedia!")
        print ("1. Get an insect fact")
        print ("2. Get a spider fact")
        print("3. Exit")

        choice = input("Enter your choice:")

        if choice == '1':
            insects = display_insect_list()
            try:
                insect_choice = int(input("Enter the number of an insect to learn more (0 to exit):"))
                if 1 <= insect_choice <= len(insects):
                    selected_insect = insects[insect_choice - 1]
                    display_insect_details(selected_insect)
                elif insect_choice == 0:
                    break
                else:
                    print("Invalid choice. Please enter a valid number.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        elif choice == '2':
            spiders = display_spider_list()
            try:
                spider_choice = int(input("Enter the number of a spider to learn more (0 to exit): "))
                if 1 <= spider_choice <= len(spiders):
                    selected_spider = spiders[spider_choice - 1]
                    display_spider_details(selected_spider)
                elif spider_choice == 0:
                    break
                else:
                    print("Invalid choice. Please enter a valid number.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid number.\n")
            
def display_insect_details(animal):
    print("\nSelected Insect:")
    print(f"Name: {animal.name}")
    print(f"Scientific Name: {animal.scientific_name}")
    print(f"Habitat: {animal.habitat}")
    print(f"Diet: {animal.diet}")
    print(f"Behavior: {animal.behavior}")
    if isinstance(animal, SpiderTable):
        print(f"Venomous: {'Yes' if animal.venomous else 'No'}")

def display_spider_details(spider):
    print("\nSelected Spider:")
    print(f"Name: {spider.name}")
    print(f"Scientific Name: {spider.scientific_name}")
    print(f"Habitat: {spider.habitat}")
    print(f"Diet: {spider.diet}")
    print(f"Behavior: {spider.behavior}")
    print(f"Venomous: {'Yes' if spider.venomous else 'No'}")

def display_insect_list():
    print("Available Animals:")
    insects = session.query(InsectTable).all()
    spiders = session.query(SpiderTable).all()
    
    for index, animal in enumerate(insects + spiders, start=1):
        print(f"{index}. {animal.name}")
    print()

def display_spider_list():
    print("Available Spiders:")
    spiders = session.query(SpiderTable).all()
    
    for index, spider in enumerate(spiders, start=1):
        print(f"{index}. {spider.name}")
    print()

if __name__ == "__main__":
    main_menu()
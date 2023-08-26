from Insects import insects, Insect
from spiders import Spiders, Spider

from lib.cli import main_menu, display_insect_details, display_spider_list, display_insect_list 
from data.database import Session, initialize_database
from data.model import InsectTable

def main():
    session = Session()
    initialize_database(session)  

    insects = session.query(Insect).all()

    while True:
        main_menu(insects)

        try:
            choice = int(input("Enter the number of an insect to learn more (0 to exit): "))
            if choice == 0:
                break

            elif 1 <= choice <= len(insects):
                selected_insect = insects[choice - 1]
                insect = session.query(Insect).filter_by(name=selected_insect.name).first()
                if insect:
                    display_insect_details(insect)
                else:
                    print("Insect details not found in the database.")
            else:
                print("Invalid choice. Please enter a valid number.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    session.close()

if __name__ == "__main__":
    main()

from lib.cli import display_home_page, display_insect_details, search_insects
from data.database import Session, initialize_database
from data.model import Insect

def search_animals_by_characteristic(keyword, insects):
    matching_insects = []
    for insect in insects:
        if (keyword.lower() in insect.habitat.lower()) or \
           (keyword.lower() in insect.diet.lower()) or \
           (keyword.lower() in insect.behavior.lower()):
            matching_insects.append(insect)
    return matching_insects

def main():
    session = Session()
    initialize_database(session)  

    insects = session.query(Insect).all()

    while True:
        display_home_page(insects)

        try:
            choice = int(input("Enter the number of an insect to learn more (0 to exit): "))
            if choice == 0:
                break
            elif choice == 4:
                search_keyword = input("Enter a characteristic keyword to search for: ")
                search_results = search_animals_by_characteristic(search_keyword, insects)
                if search_results:
                    print("Search Results:")
                    for index, insect in enumerate(search_results, start=1):
                        print(f"{index}. {insect.name}")
                    insect_index = int(input("Enter the number of the insect to view details: "))
                    if 1 <= insect_index <= len(search_results):
                        selected_insect = search_results[insect_index - 1]
                        display_insect_details(selected_insect)
                    else:
                        print("Invalid insect number.")
                else:
                    print(f"No insects found with '{search_keyword}' in their characteristics.")
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

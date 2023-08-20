from database import session
from models import Insect

def display_insect_details(selected_insect):
    print("\nSelected Insect:")
    print(f"Name: {selected_insect.name}")
    print(f"Scientific Name: {selected_insect.scientific_name}")
    print(f"Habitat: {selected_insect.habitat}")
    print(f"Diet: {selected_insect.diet}")
    print(f"Behavior: {selected_insect.behavior}")
    print()

def search_insects(criteria):
    matching_insects = session.query(Insect).filter(
        Insect.habitat.ilike(f'%{criteria}%') |
        Insect.diet.ilike(f'%{criteria}%') |
        Insect.behavior.ilike(f'%{criteria}%')
    ).all()

    if matching_insects:
        print("Matching Insects:")
        for index, insect in enumerate(matching_insects, start=1):
            print(f"{index}. {insect.name}")
        print()
    else:
        print("No insects match the search criteria.\n")



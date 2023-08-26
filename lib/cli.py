from data.database import session
from data.model import Insect

def display_insect_details(selected_insect):
    print("\nSelected Insect:")
    print(f"Name: {selected_insect.name}")
    print(f"Scientific Name: {selected_insect.scientific_name}")
    print(f"Habitat: {selected_insect.habitat}")
    print(f"Diet: {selected_insect.diet}")
    print(f"Behavior: {selected_insect.behavior}")
    print()


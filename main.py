from lib.cli import main_menu, display_insect_details, display_spider_list, display_insect_list 
from data.database import session, initialize_database

def main():
    
    initialize_database(session)  # Calls function to set up database
    main_menu()  # Calls function to start main menu
    session.close() # closes SQLAlchemy session 

if __name__ == "__main__":
    main()

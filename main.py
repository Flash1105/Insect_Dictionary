from lib.cli import main_menu, display_insect_details, display_spider_list, display_insect_list 
from data.database import session, initialize_database

def main():
    
    initialize_database(session)  
    main_menu()
    session.close()

if __name__ == "__main__":
    main()

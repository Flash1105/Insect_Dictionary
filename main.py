from lib.cli import main_menu
from data.database import initialize_database

if __name__ == "__main__":
    initialize_database()
    main_menu()

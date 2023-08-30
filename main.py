from lib.cli import main_menu
from data.database import initialize_database
from Insects import insects
from spiders import spiders

if __name__ == "__main__":
    initialize_database()
    main_menu()

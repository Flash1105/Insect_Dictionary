from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.model import Base, Insect

engine = create_engine('sqlite:///insect_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def populate_database(insects):
    for insect_data in insects:
        insect = Insect(**insect_data)
        session.add(insect)
    session.commit()



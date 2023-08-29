from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# Define Bases as tables for both 
class InsectTable(Base):
    __tablename__ = 'insects'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)

    # One-to-many relationship with facts
    facts = relationship ("AnimalFact", back_populates="insect")


class SpiderTable(Base):
    __tablename__ = 'spiders'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)
    venomous = Column(Boolean)

    facts = relationship("AnimalFact", back_populates="spider")

class AnimalFact(Base):
    __tablename__ = 'animal_facts'
    id = Column(Integer, primary_key=True)
    fact = Column(String)

# foreign key relationships
insect_id = Column(Integer, ForeignKey('insects.id'))
spider_id = Column(Integer, ForeignKey('spiders.id'))


insect = relationship("InsectTable", back_populates="facts")
spider = relationship("SpiderTable", back_populates="facts")

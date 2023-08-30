from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class AnimalFact(Base):
    __tablename__ = 'animal_facts'
    id = Column(Integer, primary_key=True)
    fact = Column(String)
    insect_id = Column(Integer, ForeignKey('insects.id'))
    insect = relationship("InsectTable", back_populates="facts")
    spider_id = Column(Integer, ForeignKey('spiders.id'))
    spider = relationship("SpiderTable", back_populates="facts")

class InsectTable(Base):
    __tablename__ = 'insects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)
    facts = relationship("AnimalFact", back_populates="insect")

class SpiderTable(Base):
    __tablename__ = 'spiders'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)
    facts = relationship("AnimalFact", back_populates="spider")

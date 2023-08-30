from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InsectTable(Base):
    __tablename__ = 'insects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)
    facts = relationship("AnimalFact", back_populates="insect")

class SpiderTable(Base):
    __tablename__ = 'spiders'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)
    venomous = Column(Boolean)
    facts = relationship("AnimalFact", back_populates="spider")

class AnimalFact(Base):
    __tablename__ = 'animal_facts'
    id = Column(Integer, primary_key=True, index=True)
    fact = Column(String)
    insect_id = Column(Integer, ForeignKey('insects.id'))
    insect = relationship("InsectTable", back_populates="facts")
    spider_id = Column(Integer, ForeignKey('spiders.id'))
    spider = relationship("SpiderTable", back_populates="facts")

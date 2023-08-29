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
    facts = relationship ("FactTable", back_populates="insect")


class SpiderTable(Base):
    __tablename__ = 'spiders'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)
    venomous = Column(Boolean)

class FactTable(Base):
    __tablename__ = 'facts'
id = Column(Integer, primary_key=True)
content = Column(String)

# foreign key relationships
insect_id = Column(Integer, ForeignKey('insects.id'))
spider_id = Column(Integer, ForeignKey('spiders.id'))


insect = relationship("InsectTable", back_populates="facts")
spider = relationship("SpiderTable", back_populates="facts")

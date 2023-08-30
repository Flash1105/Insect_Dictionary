from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
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
    predator_id = Column(Integer, ForeignKey('predators.id'))
    predator = relationship("Predator", secondary= "insect_predator_association", back_populates="insects")

class SpiderTable(Base):
    __tablename__ = 'spiders'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)
    venomous = Column(Boolean)
    predator_id = Column(Integer, ForeignKey('predators.id'))
    predator = relationship("Predator",secondary="spidder_predator_association", back_populates="spiders")


class Predator(Base):
    __tablename__='predators'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    insects = relationship("InsectTable",secondary="insect_predator_association", back_populates="predator")
    spiders = relationship("SpiderTable",secondary="spider_predator_association", back_populates="predator")

insect_predator_association = Table(
    'insect_predator_association',
    Base.metadata,
    Column('spider_id',Integer, ForeignKey('spider.id'),primary_key=True),
    Column('predator_id',Integer, ForeignKey('predators.id'), primary_key=True)
)
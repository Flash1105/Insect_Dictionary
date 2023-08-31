from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#association for many-to-many relationship
insect_predator_association = Table(
    "insect_predator_association",
    Base.metadata,
    Column("insect_id", Integer, ForeignKey("insects.id")),
    Column("predator_id", Integer, ForeignKey("predators.id"))
)

spider_predator_association = Table(
    "spider_predator_association",
    Base.metadata,
    Column("spider_id", Integer, ForeignKey("spiders.id")),
    Column("predator_id", Integer, ForeignKey("predators.id"))
)


class InsectTable(Base):
    __tablename__ = 'insects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)

    predators = relationship("PredatorTable", secondary=insect_predator_association, back_populates="insects")

class SpiderTable(Base):
    __tablename__ = 'spiders'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    scientific_name = Column(String)
    habitat = Column(String)
    diet = Column(String)
    behavior = Column(String)
    venomous = Column(Boolean)

    predators = relationship("PredatorTable",secondary=spider_predator_association, back_populates="spiders")


class PredatorTable(Base):
    __tablename__='predators'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    insects = relationship("InsectTable",secondary="insect_predator_association", back_populates="predators")
    spiders = relationship("SpiderTable",secondary="spider_predator_association", back_populates="predators")

association_table = Table(
    'insect_predator_association',
    Base.metadata, 
    Column('insect_id',Integer, ForeignKey('insects.id')),
    Column('predator_id', Integer, ForeignKey('predators.id')),
    extend_existing=True
)
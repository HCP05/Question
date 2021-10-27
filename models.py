import enum

from sqlalchemy import Column, Integer, Text, Enum, ForeignKey, Float, Table,VARCHAR

from dbSessionCreator import Base

Table.schema='testschema'


class IntensityTypes(enum.Enum):
    light = 1
    medium = 2
    rich = 3


class BodyTypes(enum.Enum):
    light = 1
    medium = 2
    full = 3


class WineColors(enum.Enum):
    red = 1
    white = 2
    rose = 3


class WineCollor(Base):
    __tablename__ = 'WineColor'
    __table_args__ = {"schema": "testschema"}
    id_wine_collor = Column(Integer, primary_key=True)
    color = Column(Enum(WineColors))


class Intensity(Base):
    __tablename__ = 'WineIntensity'
    __table_args__ = {"schema": "testschema"}
    id_wine_intensity = Column(Integer, primary_key=True)
    intensity = Column(Enum(IntensityTypes))


class Body(Base):
    __tablename__ = 'Body'
    __table_args__ = {"schema": "testschema"}
    id_wine_body = Column(Integer, primary_key=True)
    body = Column(Enum(BodyTypes))


class WineType(Base):
    __tablename__ = 'WineType'
    __table_args__ = {"schema": "testschema"}
    id_wine_type = Column(Integer, primary_key=True)
    type_of_wine = Column(VARCHAR(20))


class Wine(Base):
    __tablename__ = 'Wine'
    __table_args__ = {"schema": "testschema"}
    id_w = Column(Integer, primary_key=True)
    color = Column(Integer, ForeignKey('testschema.WineColor.id_wine_collor'))
    intensity = Column(Integer, ForeignKey('testschema.WineIntensity.id_wine_intensity'))
    pH = Column(Float)
    sugar = Column(Float)
    acidity = Column(Float)
    alcohol = Column(Float)
    tannins = Column(Float)
    body = Column(Integer, ForeignKey('testschema.Body.id_wine_body'))
    variety = Column(Integer,ForeignKey('testschema.WineType.id_wine_type'))


class Cheese(Base):
    __tablename__ = 'Cheese'
    __table_args__ = {"schema": "testschema"}
    id_c = Column(Integer, primary_key=True)
    cheese=Column(VARCHAR(20))


Pairing = Table('Pairing',Base.metadata,
                Column('id_wine', ForeignKey('testschema.Wine.id_w')),
                Column('id_cheese', ForeignKey('testschema.Cheese.id_c')),
                schema='testschema'
                )

class User(Base):
    __tablename__='User'
    __table_args__ = {"schema": "testschema"}
    id_user=Column(Integer,primary_key=True)
    username=Column(VARCHAR(20))
    password=Column(VARCHAR(20))#we must implement hashing
    phothoPath=Column(VARCHAR(30))
import enum

from sqlalchemy import Column, Integer, Text, Enum, ForeignKey, Float, Table

from dbSessionCreator import Base


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


class WineCollor(Base):
    __tablename__ = 'WineColor'
    id_wine_collor = Column(Integer, primary_key=True)
    color = Column(Enum(WineColors))


class Intensity(Base):
    __tablename__ = 'WineIntensity'
    id_wine_intensity = Column(Integer, primary_key=True)
    intensity = Column(Enum(IntensityTypes))


class Body(Base):
    __tablename__ = 'Body'
    id_wine_body = Column(Integer, primary_key=True)
    body = Column(Enum(BodyTypes))


class WineType(Base):
    __tablename__ = 'WineType'
    id_wine_type = Column(Integer, primary_key=True)
    type_of_wine = Column(Text)


class Wine(Base):
    __tablename__ = 'Wine'
    id_w = Column(Integer, primary_key=True)
    color = Column(Integer, ForeignKey('WineColor.id_wine_collor'))
    intensity = Column(Integer, ForeignKey('WineIntensity.id_wine_intensity'))
    pH = Column(Float)
    sugar = Column(Float)
    acidity = Column(Float)
    alcohol = Column(Float)
    tannins = Column(Float)
    body = Column(Integer, ForeignKey('Body.id_wine_body'))
    variety = Column(Integer,ForeignKey('WineType.id_wine_type'))


class Cheese(Base):
    __tablename__ = 'Cheese'
    id_c = Column(Integer, primary_key=True)
    cheese=Column(Text)


Pairing = Table('Pairing', Base.metadata,
                Column('id_wine', ForeignKey('Wine.id_w')),
                Column('id_cheese', ForeignKey('Cheese.id_c'))
                )

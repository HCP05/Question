from dbSessionCreator import engine,Base
from models import *

def updateDB():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def dropDB():
    Base.metadata.drop_all(engine)

def getConnection():
    return engine.connect()

#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
"""
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def core(user, passw, database):
    """the essential function
    for the operation"""
    dbase_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
                format(user, passw, database)
    engine = create_engine(dbase_uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    sesh = Session()
    Base.metadata.create_all(engine)
    cities = sesh.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    sesh.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        core(sys.argv[1], sys.argv[2], sys.argv[3])

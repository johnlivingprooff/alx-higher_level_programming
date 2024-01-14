#!/usr/bin/python3
"""
 lists all State objects, and corresponding City objects,
 contained in the database hbtn_0e_101_usa
"""
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    dbase_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
                format(argv[1], argv[2], argv[3])
    engine = create_engine(dbase_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sesh = Session()

    for state in sesh.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    sesh.close()

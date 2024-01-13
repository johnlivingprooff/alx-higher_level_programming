#!/usr/bin/python3
"""
creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sesh = Session()

    new_state = State(name="California", cities=[City(name="San Francisco")])
    sesh.add(new_state)
    sesh.commit()
    sesh.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        core(sys.argv[1], sys.argv[2], sys.argv[3])

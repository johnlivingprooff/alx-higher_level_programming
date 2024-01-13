#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
with sqlalchemy; only the first state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def core(user, passw, database):
    """the essential function
    for the operation"""
    dbase_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
                format(user, passw, database)
    engine = create_engine(dbase_uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    sesh = Session()

    states = sesh.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    sesh.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        core(sys.argv[1], sys.argv[2], sys.argv[3])

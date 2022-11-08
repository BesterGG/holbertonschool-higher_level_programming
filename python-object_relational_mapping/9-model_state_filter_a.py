#!/usr/bin/python3
''''Lists all State objects from the database hbtn_0e_6_usa'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(engine)
    session = Session()
    SQ = session.query(State).all()
    for state_name in SQ:
        if "a" in state_name.name:
            print("{}: {}".format(state_name.id, state_name.name))

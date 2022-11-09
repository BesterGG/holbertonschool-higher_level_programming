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

    AddState = State(name="Louisiana")
    session.add(AddState)
    session.commit()

    SQ = session.query(State).filter(State.name == "Louisiana")
    for i in SQ:
        print(f"{i.id}")

#!/usr/bin/python3
''''Lists all State objects from the database hbtn_0e_6_usa'''

from sys import argv
from model_city import City, Base
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    SQ = session.query(City, State).filter(State.id == City.state_id).all()
    for c, s in SQ:
        print(f"{s.name}: ({c.id}) {c.name}")

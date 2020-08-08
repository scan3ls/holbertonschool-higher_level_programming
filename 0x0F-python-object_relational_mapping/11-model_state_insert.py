#!/usr/bin/python3
""" module """

if __name__ == "__main__":

    # imports
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base

    # creates the engine
    # format("user", "passwd", "db_name")
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # creates the session
    Session = sessionmaker(bind=engine)

    # creates declarative base
    Base = declarative_base()

    # use base to create relation with db_table

    # connect to the db
    session = Session()

    # perform the sql command
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    things = session.query(State).filter(State.name == "Louisiana")
    first = things.first()
    if first is not None:
        print("{}".format(first.id))
    else:
        print("Not found")

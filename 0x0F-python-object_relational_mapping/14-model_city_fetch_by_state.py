#!/usr/bin/python3
""" module """

if __name__ == "__main__":

    # imports
    import sys
    from model_state import Base, State
    from model_city import City
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

    # creates the session
    Session = sessionmaker(bind=engine)

    # creates declarative base

    # use base to create relation with db_table

    # connect to the db
    session = Session()

    # perform the quarry
    things = session.query(City, State).join(
        State, State.id == City.state_id
        ).all()
    for item in things:
        print("{}: ({}) {}".format(
            item[1].name, item[0].id, item[0].name
            )
        )

#!/usr/bin/python3
""" module """

if __name__ == "__main__":

    # imports
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import Column, Integer, String

    # creates the engine
    # format("user", "passwd", "db_name")
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        "root", "", "hbtn_0d_usa"
    ), pool_pre_ping=True)

    # creates the session
    Session = sessionmaker(bind=engine)

    # creates declarative base
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()

    # use base to create relation with db_table
    class table(Base):
        """ class """
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True)
        name = Column(String)

        def __repr__(self):
            """ function """
            return "<State(name={},  id={}".format(
                self.name, self.id
            )

    # connect to the db
    session = Session()

    # perform the quarry
    for thing in session.query(table):
        print("({}, '{}')".format(thing.id, thing.name))

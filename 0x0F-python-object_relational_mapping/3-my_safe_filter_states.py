#!/usr/bin/python3
""" module """

if __name__ == "__main__":

    import MySQLdb

    # if script takes args
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    # end if

    # MySQLdb connect() args
    params = {
        "host": "localhost",  # Defaults to local host
        "user": "root",  # Defaults to current user
        "passwd": "",  # Defaults No password
        "db": "hbtn_0e_0_usa",  # no Default
    }

    # MySQLdb connect to database
    db = MySQLdb.connect(**params)

    # Setup cursor to execute MySQL commands
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT *
            FROM states
            WHERE states.name = %s
            ORDER BY states.id
        """, (stateName,)
    )

    # collect the stored results
    results = cursor.fetchall()

    # use the results

    # python code goes here #
    for item in results:
        print(item)

    # close cursor
    cursor.close()

    # close connection to database
    db.close()

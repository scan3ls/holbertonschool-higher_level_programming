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
        "user": username,  # Defaults to current user
        "passwd": password,  # Defaults No password
        "db": database,  # no Default
    }

    # MySQLdb connect to database
    db = MySQLdb.connect(**params)

    # Setup cursor to execute MySQL commands
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states
            ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
        """, (stateName,)
    )

    # collect the stored results
    results = cursor.fetchall()

    # use the results

    # python code goes here #
    cities = []
    for item in results:
        cities.append(item[1])
    print(*cities, sep=", ")

    # close cursor
    cursor.close()

    # close connection to database
    db.close()

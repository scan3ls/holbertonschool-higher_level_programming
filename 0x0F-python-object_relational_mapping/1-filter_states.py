#!/usr/bin/python3
""" execute mysql task with given user info on given database """

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]

    # MySQLdb connect() args
    params = {
        "host": "localhost",
        "user": username,
        "passwd": password,
        "db": database
    }

    # MySQLdb connect to database
    db = MySQLdb.connect(**params)

    # Setup cursor to execute MySQL commands
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT *
            FROM states
            WHERE INSTR(LEFT(states.name, 1), 'N') > 0
            ORDER BY states.id
        """
    )

    # collect the stored results
    results = cursor.fetchall()

    # use the results
    # python code goes here
    for item in results:
        print(item)

    # close cursor
    cursor.close()

    # close connection to database
    db.close()

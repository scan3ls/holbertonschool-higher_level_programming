#!/usr/bin/python3
""" module """

if __name__ == "__main__":

    import MySQLdb

    # if script takes args
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]

    # end if

    # MySQLdb connect() args
    params = {
        "host": "ph_host",  # Defaults to local host
        "user": "ph_user",  # Defaults to current user
        "passwd": "ph_password",  # Defaults No password
        "db": "ph_database",  # no Default
        "port": int("ph_port"),  # Defaults to 3306
        "conv": "ph conversion dict"  # Default: MySQLdb.converters.conversions
    }

    # MySQLdb connect to database
    db = MySQLdb.connect(**params)

    # Setup cursor to execute MySQL commands
    cursor = db.cursor()
    cursor.execute(
        # mysql command goes here
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

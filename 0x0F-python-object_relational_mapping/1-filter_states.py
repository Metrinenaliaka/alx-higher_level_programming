#!/usr/bin/python3
"""lists all states from database hbtn_0e_0_usa starting with N"""
import sys
import MySQLdb


def main(argv):
    """main function"""

    if len(argv) - 1 != 3:
        print("Must enter 3 arguments")
        return

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)

    db.close()


if __name__ == "__main__":

    import sys
    main(sys.argv)

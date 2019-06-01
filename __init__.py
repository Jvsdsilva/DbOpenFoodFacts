# !/usr/bin/python3
# -*- coding: Utf-8 -*
from Classes import Connection


# Main program
def main():
    con = Connection.Connection()
    con.Open_connection_MySQL()


if __name__ == "__main__":
    main()

# Autor: Luis G Rivas

import os
import sqlite3
from sqlite3 import Error
from tables import tb_list



def create_dir():
    path = os.getcwd()
    newdir = os.path.join(path, "todo/")
    try:
        if not os.path.exists(newdir):
            os.makedirs(newdir)
    except OSError:
        print(f"El directiorio {newdir} ya existe.")


def create_tables(conn, tb):
    try:
        c = conn.cursor()
        c.execute(tb)
    except Error as e:
        print(e)

 
def create_db(tb_list=tb_list):
    """ create a database connection to a SQLite database """
    path = os.path.join(os.getcwd(), "todo/", "todo.db")

    conn = None
    try:
        conn = sqlite3.connect(path)
    except Error as e:
        print(e)
    finally:
        if conn:
            for t in tb_list:
                create_tables(conn, t)
            conn.close()

 
 
if __name__ == '__main__':
    create_dir()
    create_db()
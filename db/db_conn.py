import peewee

from data.config import database_name, db_host, db_port, db_root_pass

conn = peewee.MySQLDatabase(database_name, user="root", password=db_root_pass,
                            host=db_host, port=db_port)

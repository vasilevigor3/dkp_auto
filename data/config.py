from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

db_root_pass = env.str("MYSQL_ROOT_PASSWORD")
db_port = env.int("port")
db_host = env.str("host")
database_name = env.str("database_name")

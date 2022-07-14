from clickhouse_driver import Client
client = Client('localhost')
client.execute("CREATE DATABASE atacks ENGINE = Memory COMMENT 'atakk';")
client.execute("CREATE TABLE IF NOT EXISTS atacks.atk (datetime DateTime,atk_type String) ENGINE = Log;")
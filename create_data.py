import random
import datetime
import time
from clickhouse_driver import Client
client = Client('localhost')
while (1):
    cnt = random.randint(1, 5)
    cur_atk = ''
    if cnt == 1:
        cur_atk = 'DDoS'
    if cnt == 2:
        cur_atk = 'SQL injection'
    if cnt == 3:
        cur_atk = 'Sniffing'
    if cnt == 4:
        cur_atk = 'maodzedun'
    if cnt == 5:
        cur_atk = 'XSS'
    cur_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    client.execute(f"INSERT INTO atacks.atk (*) VALUES (toDateTime('{cur_time}'), '{cur_atk}');")
    time.sleep(0.001)
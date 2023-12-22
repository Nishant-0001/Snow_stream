import json
import time

from Create.table import cursor
from Fake_data.Fake_data_genrator import generate_fake_data
from configurations.config import conn


def send_data_to_snowflake(data):
  cursor = conn.cursor()
  cursor.execute("INSERT INTO sensor_data VALUES (%s, %s, %s, %s, %s)", (data["sensor_id"], data["temperature"], data["humidity"], data["pressure"], data["timestamp"]))
  conn.commit()

# Loop and send generated data with delay
for _ in range(100000):
  data_point = generate_fake_data()
  send_data_to_snowflake(json.loads(data_point))
  #time.sleep(0.01)

cursor.close()
conn.close()

import json
import random
from datetime import datetime
import time

def generate_fake_data():
 """
 Generates a random JSON object representing sensor data.
 """
 sensor_id = random.randint(1, 1000)
 temperature = random.uniform(15.0, 30.0)
 humidity = random.uniform(40.0, 60.0)
 pressure = random.uniform(980.0, 1020.0)
 timestamp = datetime.now().isoformat()

 data = {
   "sensor_id": sensor_id,
   "temperature": temperature,
   "humidity": humidity,
   "pressure": pressure,
   "timestamp": timestamp
 }

 return json.dumps(data)




from configurations.config import conn

create_table_sql = """
CREATE TABLE IF NOT EXISTS sensor_data (
  sensor_id INTEGER,
  temperature FLOAT,
  humidity FLOAT,
  pressure FLOAT,
  timestamp STRING
);
"""

cursor = conn.cursor()
cursor.execute(create_table_sql)
conn.commit()

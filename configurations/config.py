account = ""
user = ""
password = ""
warehouse = ""
database = ""
schema = ""

conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    warehouse=warehouse,
    database=database,
    schema=schema
)

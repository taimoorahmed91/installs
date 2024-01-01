import requests
import pymysql
from datetime import datetime

def get_current_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()

    if data.get("result") == "success":
        rate = data.get("conversion_rate")
        if rate is not None:
            return rate
        else:
            return "Conversion rate not found in response."
    else:
        return "Error fetching data from the API: " + data.get("error_type", "Unknown error")

def insert_into_db(host, user, password, db, rate, table_name):
    connection = pymysql.connect(host=host, user=user, password=password, db=db)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO `{table_name}` (`usd`, `pkr`, `time`) VALUES (%s, %s, %s)"
            cursor.execute(sql, ('1', rate, datetime.now()))

        # Commit the changes
        connection.commit()
    finally:
        connection.close()

# API and DB details
api_key = '2615ea2686bba75356bb7d32'
base_currency = 'USD'
target_currency = 'PKR'
db_host = '127.0.0.1'
db_user = 'root'
db_password = 'C1sc0123@'
db_name = 'currency'
table_name = 'usdpkr'  # Table name for USD to PKR

# Get the current exchange rate
exchange_rate = get_current_exchange_rate(api_key, base_currency, target_currency)

if isinstance(exchange_rate, float):
    # Insert into database
    insert_into_db(db_host, db_user, db_password, db_name, exchange_rate, table_name)
    print(f"Inserted Exchange Rate from {base_currency} to {target_currency}: {exchange_rate}")
else:
    print("Failed to fetch exchange rate:", exchange_rate)


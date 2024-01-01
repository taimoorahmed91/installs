import requests
import datetime
import mysql.connector

# Pi-hole API URL
pi_hole_api_url = 'http://192.168.0.253:8080/admin/api.php?summaryRaw&auth=c55bdfb35600a71494fbdbebba45b624f1f6f513ba0da263b0f6479bbe36439a'

# Database connection configuration
db_config = {
    'user': 'root',
    'password': 'C1sc0123@',
    'host': '127.0.0.1',
    'database': 'pihole'
}

# Function to insert data into the database
def insert_into_db(record):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = ("INSERT INTO pihole_stats (recorded_at, domains_being_blocked, dns_queries_today, ads_blocked_today) "
                 "VALUES (%s, %s, %s, %s)")
        cursor.execute(query, record)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Sending a GET request to the API
response = requests.get(pi_hole_api_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    domains_blocked = data.get('domains_being_blocked')
    dns_queries_today = data.get('dns_queries_today')
    ads_blocked_today = data.get('ads_blocked_today')

    # Current timestamp
    current_time = datetime.datetime.now()

    # Data record to be inserted
    record = (current_time, domains_blocked, dns_queries_today, ads_blocked_today)

    # Insert data into the database
    insert_into_db(record)
    print("Data inserted into database.")
else:
    print("Failed to retrieve data from Pi-hole API")


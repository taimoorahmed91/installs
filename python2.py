import subprocess
import re
from datetime import datetime
import mysql.connector

import time
# Run the speedtest-cli command with sudo
result = subprocess.run(['sudo', 'speedtest-cli'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get the output from the command
output = result.stdout


# Write the output to output.txt, replacing any existing data
with open('/home/taimoor/installs/output.txt', 'w') as file:
    file.write(output)


# Extract the information using regular expressions
source_match = re.search(r'Testing from (.+?)(?=\.\.\.)', output)
hosted_by_match = re.search(r'Hosted by (.+?) \[', output)
download_match = re.search(r'Download: (.+) Mbit/s', output)
upload_match = re.search(r'Upload: (.+) Mbit/s', output)
delay_match = re.search(r'Hosted by .+?: (.+?) ms', output)

# Extracted information
source = source_match.group(1) if source_match else "N/A"
hosted_by = hosted_by_match.group(1) if hosted_by_match else "N/A"
download_speed = download_match.group(1) if download_match else "N/A"
upload_speed = upload_match.group(1) if upload_match else "N/A"
delay = delay_match.group(1) if delay_match else "N/A"
timestamp = datetime.now().strftime("%I:%M %p, %A, %d-%B")

# Connect to the MySQL database
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "C1sc0123@",
    "database": "speedtest"
}

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Insert the data into the database
    insert_query = "INSERT INTO speedtesting (timestamp, source, hosted_by, delay, download_speed, upload_speed) " \
                   "VALUES (%s, %s, %s, %s, %s, %s)"
    data = (timestamp, source, hosted_by, delay, download_speed, upload_speed)
    cursor.execute(insert_query, data)
    connection.commit()

    print("Data inserted into the database successfully")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()


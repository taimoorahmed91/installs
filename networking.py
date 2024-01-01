import psutil
import time

def capture_traffic():
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_recv = net_io.bytes_recv
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    return timestamp, bytes_sent, bytes_recv

def write_to_file(data, filename="network_traffic_log.txt"):
    with open(filename, "a") as file:
        file.write(f"{data[0]}, {data[1]}, {data[2]}\n")

# Example: Capture and store data every 10 seconds
try:
    while True:
        data = capture_traffic()
        write_to_file(data)
        time.sleep(10)
except KeyboardInterrupt:
    print("Stopping data capture.")


import math
import sys
import time

def haversine(coord1, coord2):
    R = 6371  # Earth radius in km
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

# Your fixed location coordinates
your_location = (50.086683535604344, 20.03085903186777)

if len(sys.argv) != 3:
    print("Usage: python script.py [latitude] [longitude]")
    sys.exit(1)

# Destination coordinates from command line arguments
destination_lat = float(sys.argv[1])
destination_lon = float(sys.argv[2])
destination_location = (destination_lat, destination_lon)

# Calculate the initial distance
initial_distance = haversine(your_location, destination_location)
print(f"Initial Distance: {initial_distance} km")

while True:
    # Fetch the current live location (if applicable)
    # live_location = get_live_location()  # Uncomment and implement if live updates are available

    # If live location updates are available, you can update the distance calculation here
    # distance = haversine(your_location, live_location)
    # print(f"Updated Distance: {distance} km")

    time.sleep(60)  # Checks every minute (or your preferred interval)


import json
from datetime import datetime

# Generate JSON data with a UTC timestamp
utc_now = datetime.utcnow()
data = {
    "Timestamp": utc_now.strftime("%d%b%Y-%H-%M"),  # Format as "16OCT2023-22-30"
    "Humidity": 79.80000305,
    "Temperature": 9.5,
    "HeatIndex": 8.58913517,
    "SoilMoisture": 1515
}

# Save data to a JSON file
with open("sensorData.json", "w") as json_file:
    json.dump(data, json_file)


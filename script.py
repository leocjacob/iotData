from influxdb_client import InfluxDBClient
import json
from datetime import datetime
import os

# Get the current date and time in UTC
created_on = datetime.utcnow().isoformat()

# InfluxDB 2 connection settings
url = os.environ.get('INFLUXDB_URL')
token = os.environ.get('INFLUXDB_TOKEN')
org = os.environ.get('INFLUXDB_ORG')
bucket = os.environ.get('INFLUXDB_BUCKET')

# Create an InfluxDB 2 client
client = InfluxDBClient(url=url, token=token, org=org)

query_api = client.query_api()

query = 'from(bucket: "' + bucket + '")' + \
        '  |> range(start: -96h)' + \
        '  |> filter(fn: (r) => r["_measurement"] == "HeatIndex" or r["_measurement"] == "Humidity" or r["_measurement"] == "SoilMoisture" or r["_measurement"] == "Temperature")' + \
        '  |> map(fn: (r) => ({ r with _time: r._time }))'

tables = query_api.query(query, org="leocj.ca")


# Initialize a dictionary to store the data
output_data = {
    "MetaData": {
        "createdOn": created_on
    },
    "Temperature": [],
    "Humidity": [],
    "HeatIndex": [],
    "SoilMoisture": []
}

# Iterate through the records and organize the data
for table in tables:
    for record in table.records:
        measurement = record.get_measurement()
        time = record.get_time().isoformat()
        value = record.get_value()
        data_point = {"dateTime": time , "value": value}
        
        if measurement == "Temperature":
            output_data["Temperature"].append(data_point)
        elif measurement == "Humidity":
            output_data["Humidity"].append(data_point)
        elif measurement == "HeatIndex":
            output_data["HeatIndex"].append(data_point)
        elif measurement == "SoilMoisture":
            output_data["SoilMoisture"].append(data_point)

# Convert the dictionary to a JSON string
json_output = json.dumps(output_data, indent=4)

# Save data to a JSON file
if(tables!=[]):
  with open("sensorData.json", "w") as json_file:
      json_file.write(json_output)  # Use write() instead of dump()
  print("Sensor Data Created.")
else:
    print("No Sensor Data")
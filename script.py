import json

# Generate JSON data
data = {"Timestamp": datetime.now().strftime("%d%b%Y-%H-%M"),"Humidity":79.80000305,"Temperature":9.5,"HeatIndex":8.58913517,"SoilMoisture":1515}

# Save data to a JSON file
with open("sensorData.json", "w") as json_file:
    json.dump(data, json_file)

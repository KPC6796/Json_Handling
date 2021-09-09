import json


with open("example.json") as json_file:
    data = json.load(json_file)
    headers = data[0].keys()

print(data)
print(headers)

for record in data:
    rec = (value for value in record.values())
    print(list(rec))


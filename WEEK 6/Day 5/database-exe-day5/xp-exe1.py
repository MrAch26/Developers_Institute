import json


json_file = 'sampleJson.json'
with open(json_file, 'r') as file_obj:
    my_family = json.load(file_obj)

print(my_family['company']['employee']['payble']['salary'])
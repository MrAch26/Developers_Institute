import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

json_file = 'xp2.json'

with open(json_file, 'w') as file_obj:
    json.dump(sampleJson, file_obj, indent=2, sort_keys=True)
   #json.dump(obj2save , destination_file)
import requests
import json



response = requests.get("https://api.chucknorris.io/jokes/random")


print(str(response.text))

# response = jsonify(data)
# response.status_code = 200
# json_file = "chuck_norris.json"

# with open(json_file, 'w') as file_obj:
#     json.dump(response, file_obj)
#    #json.dump(obj2save , destination_file)



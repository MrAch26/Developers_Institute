import psycopg2

print('line2')
HOSTNAME = 'localhost'
PORT = '5433' # check port !
USERNAME = 'postgres'
PASSWORD = 'Ba1958'
DATABASE = 'dvdrental'
print('line8')

connection = psycopg2.connect( host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, dbname=DATABASE )
print('line11')

cursor = connection.cursor()
print('line15')

query = "SELECT * FROM customer LIMIT 20;"
print('line18')

cursor.execute(query)
print('line21')

results = cursor.fetchall()

connection.close()

for item in results:
        print(item)


# # requests is working ✅

# import requests
# import json
# response = requests.get("http://api.open-notify.org/iss-now.json")

# response.json()
# data = json.loads(response.text)
 

# # EXE 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# keyValues = dict(zip(keys,values))
# print(keyValues)

# # EXE 2
# store = {
# 'name': 'Zara', 
# 'creation_date': '1975',
# 'creator_name': 'Amancio Ortega Gaona',
# 'type_of_clothes': ['men', 'women', 'children', 'home'] ,
# 'international_competitors': ['Gap', 'H&M', 'Benetton'],
# 'number_stores': '7000', 
# 'major_color': {'France' : 'blue', 'Spain' : 'red', 'US': ['pink', 'green']}
# }
# # 2
# store['number_stores'] = 2
# # print(store['number_stores'])
# # 3
# # print("The client of Zara are cool and sexy")
# # 4
# store['country_creation'] = 'Spain'
# # print(store['country_creation'])
# # 5
# store['international_competitors'].append('Desugual')
# # print(store['international_competitors'])
# # 6
# store.pop('creation_date')
# # print(store)
# # 7
# # print(store['international_competitors'][len(store['international_competitors'])-1])
# # 8
# # print('The major clothes colors in the US are :',store['major_color']['US'])
# # 9
# # print(len(store))
# # 10
# # for key, value in store.items() :
# #     print (key)
# # 11
# more_on_zara = {
#     'creation_date':'1975',
#     'number_stores':'10 000'
# }
# # print(more_on_zara)
# # 2) 1 
# store.update(more_on_zara)
# # print(store)
# # 2
# # print(store['number_stores'])

# # EXE 3
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 

# # 1

# disney_users_A = {}
# keys = range(len(users)-1)
# for i in keys:
#     if 'i' in users[i] and 'M' == users[i][0]:
#         disney_users_A[users[i]] = keys[i]
# print('user A',disney_users_A)


# # 2
# disney_users_B = dict(list(enumerate(users)))
# print('user B',disney_users_B)

# # 3
# users_sorted = sorted(users)

# disney_users_C = {}
# keys = range(len(users_sorted)-1)
# for i in keys:
#     disney_users_C[users_sorted[i]] = keys[i]
# print('user C',disney_users_C)

# #1/ print(disney_users_A) >> {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# #2/ print(disney_users_B) >> {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# #3/ print(disney_users_C) >> {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
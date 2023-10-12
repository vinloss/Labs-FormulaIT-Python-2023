users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

dict_1 = {
    "Общее количество":0
}
dict_2 = {
    "Уникальные посещения":0
}
dict_1["Общее количество"] = len(users)
dict_2["Уникальные посещения"] = len(set(users))

print(dict_1, dict_2)

# dictionary

person = {"name":"Ali","languages":["Python","C#"]}
# result = person["name"]
# print(result)
# result = person["languages"]
# print(result)
# result = person["languages"][0]
# print(result)


import simplejson as json
person_string = '{"name":"Ali","languages":["Python","C#"]}'
person_dict = {"name":"Ali","languages":["Python","C#"]}

# # JSON string to Dict
# result = json.loads(person_string)
#
# print(result)
# print(type(result))


# with open("person.json") as f:
#     data = json.load(f)
#     print(data)
#     print(data["name"])
#     print(data["languages"])


# # Dict to JSON string


# result = person_dict
# print(result)
# print(type(result))
# result = json.dumps(person_dict)
# print(result)
# print(type(result))
# print(result["name"]) # hata verir artik

# with open("person.json","w") as f:
#     json.dump(person_dict,f)

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4, sort_keys=True)
print(person_dict)
print(result)

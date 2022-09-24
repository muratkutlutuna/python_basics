# import simplejson as json
#
# print(json.__file__)

import requests as req
import simplejson as json

result = req.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)
# print(result)
#
# print(type(result))
# print(result[0]["title"])

# for i in result:
#     print(i["title"])

for i in result:
    if i["userId"] == 1:
        print(i["title"])





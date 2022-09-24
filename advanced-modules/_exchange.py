import requests as req
import simplejson as json


url = "https://api.apilayer.com/currency_data/convert?to=to&from=from&amount=amount"
#
bozulan_doviz = input("bozulan doviz turu: ")
alinan_doviz = input("alinan doviz turu: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz?"))
#
# result = req.get(url + bozulan_doviz)
# result = json.loads(result.text)
# print("1 {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))
result = req.get(url,miktar,bozulan_doviz,alinan_doviz)

print(result.text)
# payload = {}
# headers= {
#   "apikey": "{API-KEY}"
# }
#
# response = req.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text




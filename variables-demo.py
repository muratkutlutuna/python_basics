"""
    1-Bir musterinin asagidaki bilgileri icin degisken olusturunuz
    mustari adi
    musteri souadi
    musteri ad + soyad
    musteri cinsiyet
    musteri tc kimlik
    musteri dogum yili
    musteri adres bilgisi
    musteri yasi

"""
from pprint import pprint

customerName = 'Ali'
customerSurname = 'Yilmaz'
customerNameSurname = customerName+' '+customerSurname
customerGender = True #erkek
customerIDNumber = '12312414'
customerBirthYear = 1990
customerAddres = 'Baker Street 911'
customerAge = 2022-customerBirthYear
# print(customerAge)


"""
    20 asagidaki siparislerin toplam bilgisini hesaolayiniz.
    siparis 1 => 110 USD
    siparis 2 => 1100.5 USD
    siparis 3 => 359.95 USD
"""
order1 = 110
order2 = 1100.5
order3 = 359.95
total = order3+order2+order1
print("total",total)
print('sum =',order3+order2+order1)

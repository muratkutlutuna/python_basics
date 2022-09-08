# 1- Gonderilen bir kelimeyi belirtilen kez ekranda gosteren fonksiyonu yazin.
# def kelimeyiYazdir(kelime,adet):
#     print(kelime * adet)
#
#
# kelimeyiYazdir('merhaba\n',10)
# 2- Kendine gonderilen sinirsiz sayidaki parametreyo bir listeye ceviren fonksiyonu
# def listeyeCevir(*args):
#     list=[]
#     for t in args:
#         list.append(t)
#     return list
#
#
# print(listeyeCevir(3, 23, 8, 'dsfgdg', 34, True, "sdfs", 32))
# 3- Gonderilen 2 sayi arasindaki tum asal sayilari bulun.
# sayi1 = int(input('sayi1:  '))
# sayi2 = int(input('sayi2:  '))
# def aradakiAsalSayilariBul(a,b):
#     for t in range(a,b+1):
#         if t>1:
#             for l in range(2,t):
#                 if t%l==0:
#                     break
#             else:
#                 print(t)
#
# aradakiAsalSayilariBul(sayi1,sayi2)
# 4- Kendisine gonderilen bir sayinin tam volenlerini bir liste seklinde donduren fonksiyonu yazalim

def tamBolenleriBul(sayi):
    tamBolenler=[]

    for i in range(2,sayi):
        if sayi%i==0:
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(12))










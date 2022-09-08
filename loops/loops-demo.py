'''
    1-100 arasinda rastgele uretilecek bir sayiyi asagi yukari
    ifadeleri ile buldurmaya calisin.(hak = 5)
    ** "random modulu" icin "python random" seklinde arama yapin.
    ** 100 uzerinden puanlama yapin. Her soru 20 puan.
    ** Hak bilgisini kullanicidan alin ve her soru belirtilen
    can sayisi uzerinden hesaplansin.
'''
#import random
# hak=3
# tahmin=222
# sayi=111
# puan=0
# print(f'sinav basladi lk sayimiz geliyor')
# while puan<=100 and hak>=0:
#     while tahmin!=sayi:
#         hak -= 1
#         sayi = random.randint(0, 100)
#         tahmin=int(input('sisce sayi kac?'))
#         if sayi==tahmin:
#             puan+=20
#             if hak<0:
#                 break
#             continue
#         else:
#             if sayi<tahmin:
#                 print('sayi daha kucuk')
#             else:
#                 print('sayi daha buyuk')
#         print(f'sayi: {sayi}, puaniniz:{puan}, hakkiniz {hak}')
# if hak==0:
#     print(f'hakkiniz bitti, puaniz: {puan}')
# else:
#     print(f'puaniniz {puan}, tebrikler!!')
import random
sayi = random.randint(1,10)
can=int(input('kac hak kullanmak istersiniz?:  '))
hak = can
sayac = 0
puan=100

while hak>0:

    if sayac>5:
        print(f'puaniniz bitti. Tutulan sayi : {sayi}')
        break

    hak-=1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac} defada bildiniz. Toplam puaniniz: {puan - (20) * (sayac-1)}')
        break
    elif sayi>tahmin:
        print('yukari')
    else:
        print('asagi')

    if hak == 0:
        print(f'hakkiniz bitti. Tutulan sayi : {sayi}')







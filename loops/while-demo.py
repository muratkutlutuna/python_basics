# sayilar = [1,3,5,7,9,12,19,21]
#
# # 1: sayilar listesini while ile ekrana yazdirin.
# x=0
# print(x)
# while x<len(sayilar):
#     print(sayilar[x])
#     x+=1
# # 2: Baslangic ve bitis degerlerini kullanicidan
# # alip aradaki tum tek sayilari ekrana yazdirin.
# baslangic=input('Lutfen baslangic sayisini giriniz.')
# bitis = input('Lutfen bitis sayisini giriniz')
# print('Baslangictan bitise kadarki tek sayilar asagidaki gibidir.')
# t = int(baslangic)
# while t<=int(bitis):
#     if t%2==1:
#         print(t)
#     t+=1
# print('bitti...')
# # 3: 1-100 arasinndaki sayilari azalan sekilde yazdirin.
# counter=0
# while counter>0:
#     print(counter)
#     counter-=1
# # 4: Kullanicidan alacaginiz 5 sayiyi ekranda sirali bir
# # sekilde yazdirin.
# numbers = []
# numbers.append(int(input('birinci sayiyi giriniz')))
# numbers.append(int(input('ikinci sayiyi giriniz')))
# numbers.append(int(input('ucnci sayiyi giriniz')))
# numbers.append(int(input('dordunci sayiyi giriniz')))
# numbers.append(int(input('besinci sayiyi giriniz')))
# print(numbers)
# numbers.sort()
# cntr=0
# while cntr< len(numbers):
#     print(numbers[cntr])
#     cntr+=1
# 5: Kullanicidan alacaginiz sinirsiz urun bilgisini urunler
# listesi icinde saklayin
#   ** urun sayisini kullaniciya sorun.
len=int(input('Lutfen urun sayisini giriniz.'))
#   **dictionary listesi yapisi (name, price) seklinde olsun.
#   **urun ekleme islemi bittiginde urunleri ekranda
#   while ile listeleyin.
countr=0
urunler=[]
while countr<len:
    countr+=1
    name=input('Lutfen gireceginiz urunun adini giriniz')
    price = input('Lutfen girdiginiz urunun fiyatini giriniz.')
    urunler.append({
        countr:{
        'isim':name,
        'fiyat':price
    }})
    print(f'Girilen urun: {name},fiyati: {price} ')
print(f'{len} miktarindaki tum urunleri girdiniz')
for urun in urunler:
    print(f'urunleriniz: {urun} tesekkurler')
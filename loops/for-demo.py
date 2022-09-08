sayilar=[1,3,5,7,9,12,19,21]
#1
sayilar2=[]
for n in sayilar:
    if n%3==0:
        sayilar2.append(n)
print(sayilar2)
#2
toplam=0
for n in sayilar:
    toplam=toplam+n
print(toplam)
#3
tek=[]
for n in sayilar:
    if n%2==1:
        tek.append(n**2)
print(tek)
#4
besKarakterli=[]
sehirler=['kocaeli','istanbul','ankara','izmir','rize']
for n in sehirler:
    if len(n)<=5:
        besKarakterli.append(n)
print(besKarakterli)
#5

urunler=[
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'},
]
top=0
for n in urunler:
    for key,value in n.items():
        if key=='price':
            top=top+int(value)
print(top)
#6
# besBinAlti=[]
# for n in urunler:
#     for key,value in n.items():
#         if key=='price':
#             if int(value)<=5000:
#                 besBinAlti.append(n)
# print(besBinAlti)
for urun in urunler:
    if (int(urun['price'])<=5000):
        print(urun['name'])
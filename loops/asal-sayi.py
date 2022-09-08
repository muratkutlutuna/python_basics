'''
soru: Girilen bir sayinin asal olup olmadigini bulun.
**Asal sayi 1 ve kendisi haric tam boleni olmayan sayilara denir.
'''

t = int(input('lutfen bir sayi giriniz:  '))
asalMi=True
if t==1:
    asalMi=False
    
for y in range(2,t):
    if t%y!=0:
        asalMi=False
        break

if asalMi:
    print(f'verilen {t} sayisi asaldir')
else:
    print(f'verilen {t} sayisi asal degildir')

#1
isim='kutlu'#input('isim: ')
yas=31#int(input('yas: '))
eg='ilkogretim'#input('egitim durumu: ')
if yas>18:
    if eg=='lise' or eg=='universite':
        print('Ehliyet alabilirsiniz')
    else:
        print('egitim durumunuz yetersiz')
else:
    print('yasiniz kucuk')

#2
yazili1=13
yazili2=87
sozlu=79
ortalama=(yazili1+yazili2+sozlu)/3
if 0<ortalama<24:
    print('not ortalamaniz: 0')
elif ortalama<44:
    print('not ortalamaniz: 1')
elif ortalama < 54:
    print('not ortalamaniz: 2')
elif ortalama < 69:
    print('not ortalamaniz: 3')
elif ortalama < 84:
    print('not ortalamaniz: 4')
elif ortalama < 100:
    print('not ortalamaniz: 5')
else:
    print('lutfen gecerli bir deger giriniz')

#3
import datetime
# days = int(input('araciniz kac gundur trafikte: '))

t = input('Lutfen tarihi giriniz (2019/8/9): ')
t=t.split('/')
print(t[0])
print(t[1])
print(t[2])
trafigeCikis = datetime.datetime(int(t[0]),int(t[1]),int(t[2]))
simdi = datetime.datetime.now()
fark=simdi-trafigeCikis
days=fark.days

if days<=365:
    print('1.servis araligi')
elif days>365 and days<=365*2:
    print('2.servis araligi')
elif days>365*2 and days<365*3:
    print('2.servis araligi')
else:
    print('Hatali sure bilgisi')


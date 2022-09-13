import re

liste = ["1","2","5a","10b","abc"]

# 1:Liste elemanlari icindeki sayisal degerleri bulunuz.
liste2=[]
for d in liste:
    try:
        int(d)
    except:
        pass
    else:
        liste2.append(d)
print(liste2)

# 2: kullanici 'q' degerini girmedikce aldiginiz her inpiputun sayi
# oldugndan emin olunuz aksi halde hata mesaji yazin.
while True:
    t = input('sayi giriniz ya da cikmak icin q ya basiniz: ')
    try:
        if t=='q':
            raise Exception('cikis yaptiniz')
        int(t)
    except ValueError as e:
        print('lutfen sayi giriniz')
    except Exception as ex:
        print(ex)
        break
    else:
        print('sayi girdiniz')
        break
# 3: Girilen parola icinde turkce karakter hatasi veriniz.

def password(psw):
    if not re.search('[A-Za-z]',psw):
        raise Exception('please input a valid value')
    else:
        print('password is valid')

psw = input('Please enter a valid password: ')
while True:
    try:
        password(psw)
    except Exception as exc:
        print(exc)
    else:
        break

# 4: Faktoriyel fonksiyonu olusturup fonksiyona gelen deger icin
# hata mesajlari verin.

def faktoriyel(n):
    f = 1
    import re
    if not re.search("[0-9]", str(n)):
        raise Exception("you didn't input a number")
    else:
        for i in range(int(n)):
            f *= i
        print('you did input a number')
        return f


while True:
    try:
        faktoriyel(3)
    except Exception as e:
        print(e)
    else:
        break

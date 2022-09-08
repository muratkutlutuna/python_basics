# 1- Girilen iki sayidan hangisi buyuktur
a = int(input('a: '))
b = int(input('b: '))
result=(a>b)
print(f'a: {a} b: {b} den buyuktur: {result}')
# 2- Kullanicidan 2 vize (%60) ve final(40%) notunu alip ortalama hesaplayiniz
#    Eger ortalama 50 ve ustundeyse gecti degilse kaldi yazdirin
vize1=float(input('vize 1 : '))
vize2=float(input('vize 2 : '))
final=float(input('final : '))
ortalama=float((vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4))
print(f'not ortalamaniz : {ortalama} ve dersten gecme durumunuz: {ortalama>50}')
# 3- Girilen bir sayinin tek mi cift mi oldugunu yazdirin.
sayi=int(input('sayi: '))
tekcift = (sayi%2==0)
print(f'girilen sayi cift olma durumu {tekcift}')

# 4- Girilen bir sayinin negatif pozitif durumunu yazdirin
sayi = int(input('sayi: '))
pizitifmi = sayi>0
print(f'sayinin pozitif olma durumu {pizitifmi}')

# 5- Parola ve email bilgisini isteyip dogrulugunu kontrol ediniz
#    (email: email@sadikturan.com parola:abc123)
email= 'email@sadikturan.com'
parola='abc123'
girilenEmail = input('Lutfen email adresinizi giriniz: ')
girilenPassword = input(f'Lutfen passswordunuzu giriniz: ')
print(f'Emailinizin dogrulugu: {girilenEmail.lower().strip()==email}, passwordunuzun dogrulugu: {girilenPassword.lower().strip()==parola}')

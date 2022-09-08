def sayHello(name = 'user'):
    return 'Hello '+name

msg = sayHello('cinar')
print(msg)

def total(num1,num2):
    return num1+num2

result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2019 - dogumYili

ageCina = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)

print(ageCina,ageAda,ageSena)

def emekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    :param dogumYili: 1983
    :param isim: 'Ahmet'
    :return:emekliliginize 29 yil kaldi
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65-yas

    if emeklilik > 0:
        print(f'emekliliginize {emeklilik} yil kaldi')
    else:
        print('zaten emekli oldunuz')

emekliligeKacYilKaldi(1983, 'Ahmet')
print(help(emekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))
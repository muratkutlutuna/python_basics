# Bankamatik Uygulamasi

SadikHesap = {
    'ad': 'Sadik Turan',
    'hesapNo':'12345435',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo':'12343445',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap,miktar):
    print(f'Merhaba {hesap["ad"]}')

    if (hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print('paranizi alabilirsiniz')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye']+hesap['ekHesap']
        if (toplam>=miktar):
            ekHesapKullanimi = input('ek hesap kullanilsin mi (e/h)')
            if ekHesapKullanimi=='e':
                ekHesapKullanilacakMiktar = miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekHesapKullanilacakMiktar
                print('paranizi alabilirsiniz')
                bakiyeSorgula(hesap)
            else:
                print(f'{hesap["hesapNo"]} nolu hesabinizda {hesap["bakiye"]} bulunmaktadir.')
        else:
            print('uzgunuz bakiye yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f'{hesap["hesapNo"]} nolu hesabinizda {hesap["bakiye"]} TL bulunmaktadir. Ek hesap limitiniz ise {hesap["ekHesap"]} bulunmkatadir')


paraCek(SadikHesap,3000)
paraCek(SadikHesap,1000)
bakiyeSorgula(SadikHesap)

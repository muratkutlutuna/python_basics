'''
ogrenciler = {
    '120': {
        'ad':'Ali',
        'soyad':Yilmaz,
        'telefon':'532 000 00 01'
        },
    '125': {
        'ad':'Can',
        'soyad':Korkmaz,
        'telefon':'532 000 00 02'
        },
    '128': {
        'ad':'Volkan',
        'soyad':Yukselen,
        'telefon':'532 000 00 03'
        },
}
 1- Bilgileri verilen ogrencileri kullanicidan aldiginiz biligilerle dictionary icinde saklayiniz.

 2- Ogrenci numarasini killanicidan alip ilgili ogrenci bilgisini gosterin.
'''

ogrenciler={}
ogrenciNo=input("lutfen ogrenci numaranizi giriniz?")
isim = input("lutfen isminizi giriniz?")
soyisim = input("lutfen soyisminizi giriniz?")
telefon = input("Lutfen telefon numaranizi giriniz")
# ogrenciler[ogrenciNo]={
#     'ad':isim,
#     'soyad':soyisim,
#     'telefon':telefon
# }
ogrenciler.update({
    ogrenciNo:{
        'ad':isim,
        'soyad':soyisim,
        'telefon':telefon
    }
})

ogrenciNo=input("lutfen ogrenci numaranizi giriniz?")
isim = input("lutfen isminizi giriniz?")
soyisim = input("lutfen soyisminizi giriniz?")
telefon = input("Lutfen telefon numaranizi giriniz")
ogrenciler.update({
    ogrenciNo:{
        'ad':isim,
        'soyad':soyisim,
        'telefon':telefon
    }
})
ogrenciNo=input("lutfen ogrenci numaranizi giriniz?")
isim = input("lutfen isminizi giriniz?")
soyisim = input("lutfen soyisminizi giriniz?")
telefon = input("Lutfen telefon numaranizi giriniz")
ogrenciler.update({
    ogrenciNo:{
        'ad':isim,
        'soyad':soyisim,
        'telefon':telefon
    }
})
ogrenciNo=input("lutfen ogrenci numaranizi giriniz?")
isim = input("lutfen isminizi giriniz?")
soyisim = input("lutfen soyisminizi giriniz?")
telefon = input("Lutfen telefon numaranizi giriniz")
ogrenciler.update({
    ogrenciNo:{
        'ad':isim,
        'soyad':soyisim,
        'telefon':telefon
    }
})
print(ogrenciler)
print('*'*50)
no=input("ogrenci no giriniz?")
print(f'aradiginiz {no} nolu ogrencinin adi: {ogrenciler[no]["ad"]}, soyadi: {ogrenciler[no]["soyad"]}, telefonu: {ogrenciler[no]["telefon"]}.')
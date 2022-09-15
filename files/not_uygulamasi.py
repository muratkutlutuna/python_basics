def not_hesapla(satir):
    satir=satir[:-1]
    adSoyadNotlar = satir.split(":")
    notlar=adSoyadNotlar[1]
    notlar=notlar.strip().split(",")
    sum=int(notlar[0])+int(notlar[1])+int(notlar[2])
    avarage= sum / len(notlar)

    if avarage>=90 and avarage<=100:
        harf = "AA"
    elif avarage>=85 and avarage<=89:
        harf = "BA"
    elif avarage>=80 and avarage<=84:
        harf = "BB"
    elif avarage>=75 and avarage<=79:
        harf = "CB"
    elif avarage>=70 and avarage<=74:
        harf = "CC"
    elif avarage>=65 and avarage<=69:
        harf = "DC"
    elif avarage>=60 and avarage<=64:
        harf = "DD"
    elif avarage>=55 and avarage<=59:
        harf = "FD"
    else:
        harf = "FF"

    return adSoyadNotlar[0] + ":" + harf+"\n"


def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input('ogrenci adi : ')
    soyad = input('ogrenci soyadi : ')
    not1 = input('ogrenci not 1 : ')
    not2 = input('ogrenci not 2 : ')
    not3 = input('ogrenci not 3 : ')

    with open("sinav_notlari.txt","a",encoding="utf-8")as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')


def notlari_kayit_et():
    with open('sinav_notlari.txt',"r",encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input('1- Notlari oku\n2 - Not Gir\n3 - Notlari Kayit Et\n4 - Cikis\n')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kayit_et()
    else:
        break
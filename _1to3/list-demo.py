# 1- "BMW, Mercedes, Opel, Mazda" elemanlarina sahip bir liste olusturunuz.
arabalar=['BMW','Mercedes','Opel','Mazda']
print(arabalar)
# 2- Liste kac elemanlidir ?
print(len(arabalar))
# 3- Listenin ilk ve son elemani nedir?
print(arabalar[0])
print(arabalar[-1])
# 4- Mazda degerini toyota ile degistirini?
arabalar[-1]='Toyota'
print(arabalar)
# 5- Mercedes listenin bir elemani midir?
print('Mercedes' in arabalar)
print('Mercedess' in arabalar)
# 6- Listenin -2 indexindeki deger nedir?
print(arabalar[-2])
# 7- Listenin ilk 3 elemanini alin.
print(arabalar[0:3])
print(arabalar[:3])
print(arabalar[-2:])
print(arabalar[:-1])
# 8- Listenin son 2 elemai yerine "Toyota" ve "Renault" degerlerini ekleyin
arabalar[-2:]=['Toyota','Renault']
print(arabalar)
# 9- Listenin uzerine "Audi" ve "Nissan" degerlerini ekleyin
arabalar= arabalar +['Audi','Nissan']
print(arabalar)
# 10- Listenin son elemanini silin.
del arabalar[-1]
print(arabalar)
# 11- Liste elemanlarini tersten yazdiriniz.
print(arabalar[::-1])
# 12- Asagidaki verileri bir liste icinde saklayiniz.

        # studentA: Yigit Bilgi 2010, (70,60,70)
        # studentB: Sena Turan 1999, (80,80,70)
        # studentC: Ahmet Turan 1998, (80,70,90)
studentA = ['Yigit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet', 'Turan',1998,[80,70,90]]

students=[studentA,studentB,studentC]

# 13- Liste elemanlarini ekrana yazdiriniz
print(f"{studentA[0]} {studentA[1]} {2022-studentA[2]} ortalamasi = {(studentA[-1][0]+studentA[-1][1]+studentA[-1][2])/3}")
print(students)

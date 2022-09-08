names = ['Ali','Yagmur','Hakan','Deniz']
years = [1998, 2000,1998,1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz
# names=names+['Cenk']
names.append('Cenk')
print(names)
# 2- "Sena" degerini listenin basina ekleyiniz.
# names = ['Sema']+names
# names.insert(len(names),'Mehmet')
names.insert(0,'Sena')
print(names)
# 3- "Deniz" ismini listeden siliniz.
# names.remove('Deniz')
# print(names)
# 4- "Deniz" isminin indeksi nedir?
print(names.index('Deniz'))
print(names)
# 5- "Ali" listenin bir elemani midir?
print('Ali' in names)
# 6- Liste elemanlarini ters cevirin.
print(names[::-1])
print(names[::1])
names.reverse()
print(names)
# 7- Liste elemanlarini alfabetik olarak siralayiniz.
names.sort()
print(names)
# 8- years listesini rakamsal buyukluge gore siralayiniz
years.sort()
print(years)
# 9- str = "Chevrolet, Dacia" karakter dizisini listeye ekleyiniz.
str = "Chevrolet, Dacia"
str=str.split(', ')
print(str)
# 10- years dizisinin en buyuk ve en kucuk elemani nedir?
print(max(years))
print(min(years))
# 11- years dizisinin kac tane 1998 degeri vardir?
print(years.count(1998))
# 12- years dizisinin tum elemanlarini siliniz.
years.clear()
print(years)
# 13- kullanicidan alacaginiz 3 tane marka bilgisin bir listede saklayiniz.
brands=[input("Enter a brand name: ")]
brands.append(input("Enter a brand name: "))
brands.append(input("Enter a brand name: "))
print(brands)
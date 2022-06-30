website = "http://www.sadikturan.com"
course = "Python Kursu: Bastan Sona Python Progamlama Rehberiniz (40 saat)"

# 1- ' Hello World ' karakter dizisinin bas ve sondaki bosluk karakterlerini silin.
hw = " Hello World "
result = ' Hello World '.strip()
result = ' Hello World '.lstrip()
result = ' Hello World '.rstrip('rld ')

print(result)
print(hw.strip())
# 2- 'www.sadikturan.com' icindeki sadikturan yazisi haricindeki her karakteri silin.
print(website[11:21])
print(website.strip('htp/:w.com'))
# 3- 'course' karakter duizisinin tum karakterlerini kucuk harf yapin
print(course.lower())
# 4- 'website' icinde kac tane a karakteri vardir ? (count('a'))
print(website.count('a'))
# 5- 'website' www" ile baslayip com ile bitiyor mu?
basliyormu = website.startswith("www\"")
print(f"website www\" ile basliyor mu? = {basliyormu}")
bitiyormu = website.endswith("com")
print(f"website .com ile bitiyor mu? = {bitiyormu}")
# 6- 'website' icinde '.com' ifadesi var mi?
comVarMi = website.__contains__(".com")
print(website.find('.com'))
print(comVarMi)
# 7- 'course' icindeki karakterlerin hepsi alfabetik mi?
print(course.isalpha())
# 8- 'contents' ifadesini satirda 50 karakter icine yerlestirip sag ve soluna * ekleyiniz.
str = 'contents'
print(str.ljust(50,'*'))
print(str.rjust(50,'*'))
print(str.center(50, '*'))
# 9- 'course' karakter dizisindeki tum bosluk karakterlerini '-' ile degistirin.
print(course.replace(" ", "-"))
print(course.replace(' ','-',5))
# 10- 'Hello World' karakter dizisinin 'World ifadesini 'There' olarak degistirin
print(hw.strip().replace("World", "There"))
# 11- 'course' karakter dizisini bosluk karakterlerinden ayirin.
split = course.split(" ")
print(split)

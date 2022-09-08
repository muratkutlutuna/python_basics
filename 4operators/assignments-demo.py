x, y, z = 2, 5, 107
numbers = 1, 5, 7, 10, 6

# 1- Kullanicidan aldiginiz 2 sayinin carpimi ile x,y,z toplaminin farki nedir?
a=int(input("lutfen 1. sayiyi giriniz"))
b=int(input("lutfen 2. sayiyi giriniz"))
result=(a*b)-(x+y+z)
print(result)
# 2- y'nin x'e kalansiz bolumunu heesaplayiniz.
result=y//x
print(result)
# 3- (x,y,z) toplaminin mod 3'u nedir?
toplam=(x+y+z)
result=toplam%3
print(result)
# 4- y'nin x. kuvvetini hwsaplayiniz.
result=y**x
print(result)
# 5- x, *y, z = numbers islemine gore z'nin kupu kactir?
x, *y, z = numbers
result=z**3
print(result)
# 6- x, *y, z = numbers islemine gore y'nin degerleri toplami kactir?
x, *y, z = numbers
result=y[0]+y[1]+y[2]
print(result)

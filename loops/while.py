numbers = [1,2,3,4,5]
# 1-100 e kadar
x = 0
while x<=100:
    if x % 2==1:
        print(f'sayi tek: {x}')
    else:
        print(f'sayi cift: {x}')
    x+=1

print("Bitti..")

name = '' # False

while not name.strip():
    name = input('isminizi giriniz: ')

print(f'merhaba {name}')

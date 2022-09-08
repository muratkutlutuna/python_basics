#1
x=4#int(input("lutfen bir sayi giriniz"))
result=x>0and x<100
print(result)
#2
result2 = x>0and x%2==0
print(f'girilen syi cift ve sifirdan buyuk mu : {result2}')
#3
email="as.da@gmailcom"
pwd="asd1234f"
result3=email.__contains__('@')and email.find(".", (email.find('@')), len(email)-1)and len(pwd)>=8
print(result3) #????
#4
sayi1=1#int(input("sayi1 i giriniz"))
sayi2=2#int(input("sayi2 i giriniz"))
sayi3=3#int(input("sayi3 i giriniz"))
result4=sayi1>sayi2 and sayi1>sayi3
print(f'sayi1 en buyuk sayidir: {result4}')
result5=sayi2>sayi1 and sayi2>sayi3
print(f'sayi2 en buyuk sayidir: {result5}')
result6=sayi3>sayi2 and sayi3>sayi1
print(f'sayi3 en buyuk sayidir: {result6}')
#5
vize1=float(input('vize 1 : '))
vize2=float(input('vize 2 : '))
final=float(input('final : '))
ortalama=float((vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4))
result7=(ortalama>=50) or (final>=70)
print(f'not ortalamaniz : {ortalama} ve dersten gecme durumunuz: {result7}')
#6
name = input('adiniz: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))
index = (kg)/(hg**2)
zayif = (index>=0)and(index<=18.4)
normal = (index>18.4)and(index<=24.9)
kilolu = (index>24.9)and(index<=29.9)
obez = (index>=29.9)and(index<34.9)
print(f'{name} kilo indexin: {index} ve kilo degerlendirme zayif: {zayif}')
print(f'{name} kilo indexin: {index} ve kilo degerlendirme normal: {normal}')
print(f'{name} kilo indexin: {index} ve kilo degerlendirme kilolu: {kilolu}')
print(f'{name} kilo indexin: {index} ve kilo degerlendirme obez: {obez}')


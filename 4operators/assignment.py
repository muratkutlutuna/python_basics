# x=5
# y=10
# z=20
x,y,z=5,16,20

# x,y= y,x
x+=5# x=x+5
x-=5# x=x-5
x*=5# x=x*5
x/=5# x=x/5
x%=5# x=x%5
y//=5# y=y//5 tam bolmek icin 16 da 5 3 tanedir gibi
y**=5# y=y**5 uzeri isaretidir, 3 uzeri 5 = 243
# y**=z# y=y**z

# print(x,y,z)

values = 1,2,3
print(values)
print(type(values))
x,y,z = values
print(x,y,z)

# values = 1,2
# print(values)
# print(type(values))
# x,y,z = values# hata verir
# print(x,y,z)
#
# values = 1,2,3,4,5
# print(values)
# print(type(values))
# x,y,z = values# hata verir
# print(x,y,z)

values = 1,2,3,4,5
print(values)
print(type(values))
x,y,*z = values# hata verir
print(x,y,z)
print(x,y,z[2])
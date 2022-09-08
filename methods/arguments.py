# def changeName(n):
#     n = 'ada'
#
# name = 'yigit'
#
# changeName(name)
# print(name)
#
# def change(n):
#     n[0] = 'istanbul'
#
# sehirler = ['ankara', 'izmir']
# # change(sehirler)
# n = sehirler[:] #slicing
# n[0] = 'istanbul'
# print(sehirler)
# print(n)
#
# def change1(n):
#     n[0] = 'istanbul'
#
# sehirler = ['ankara','izmir']
# change(sehirler[:])
# print(sehirler)


# def add(a,b,c=0):
#     return sum((a,b))
#
# print(add(10,20))
# print(add(10,20,30))

# def add(*params):
#     print(params)# gonderdigimiz butun elemanlari bir tuple listesi ile yazdirir
#     print(params[0])
#     return sum((params))
#
#
# print(add(10, 20))
# print(add(10, 20, 30))


# def add(*params):
#     sum=0
#
#     for t in params:
#         sum+=sum+t
#     return sum
#
#
# print(add(10, 20))
# print(add(10, 20, 30))

def displayUser(**args):
    print(type(args)) # dictionary
    for key, value in args.items():
        print('{} is {}'.format(key,value))



displayUser(name='Cinar', age=2, city = 'Istanbul')
displayUser(name='Ada', age=12, city = 'Kocaeli', phone = '1231244')
displayUser(name='Yigit', age=14, city = 'Ankara', phone = '123124124')


def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1='value 1',key2='value 2', key3='value 3')

























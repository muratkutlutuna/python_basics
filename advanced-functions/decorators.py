# def my_decorator(func):
#     def wrapper():
#         print("fonksiyondan once islemler")
#         func()
#         print("fonksiyondan sonraki islemler")
#     return wrapper
#
# def sayHello():
#     print("Hello")
#
# def sayGreeting():
#     print("greeting")
#
# sayHello = my_decorator(sayHello)
# # sayGreeting = my_decorator(sayGreeting)
# sayHello()
# # sayGreeting()


# def my_decorator(func):
#     def wrapper():
#         print("fonksiyondan once islemler")
#         func()
#         print("fonksiyondan sonraki islemler")
#     return wrapper
#
# @my_decorator
# def sayHello():
#     print("Hello")
#
# sayHello()


# def my_decorator(func):
#     def wrapper(name):#this one should also take parameter
#         print("fonksiyondan once islemler")
#         func(name)
#         print("fonksiyondan sonraki islemler")
#     return wrapper
#
# @my_decorator
# def sayHello(name):
#     print("Hello",name)
#
# sayHello("Ali")


import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " +func.__name__+" "+ str(finish - start) + " saniye surdu\n")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(3)
toplama(2,7)


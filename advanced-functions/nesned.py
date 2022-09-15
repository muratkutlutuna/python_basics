# def greeting(name):
#     print('hello', name)

# print(greeting('ali'))
# print(greeting)#<function greeting at 0x7fd334c7cdc0>

# sayHello = greeting
#
# print(sayHello)#<function greeting at 0x7ff3d3e13dc0>
# print(greeting)#<function greeting at 0x7ff3d3e13dc0>

# print(greeting('Ali'))
# print(sayHello('Ali'))

# del sayHello
# print(greeting)
# print(sayHello)


# encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2=inner_increment(num1)
#     print(num1,num2)
#
# outer(10)
# # inner_increment(10) getirmez cunku encapsule edilmis


def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")

    if not number>=0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number<=1:
            return 1
        return number * inner_factorial(number-1)
    return inner_factorial(number)
try:
    print(factorial(-0.3))
except Exception as e:
    print(e)




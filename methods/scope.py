# #global scope
# x='global x'
#
# def function():
#     #local scope
#     x = 'local x'
#     print(x)
#
# function()
# print(x)

# global scope
x = 'global x'


def function():
    # local scope
    print(x)


function()
print(x)

###############################

name = 'Cinar'


def changeName(new_name):
    name = new_name
    print(name)


changeName('Ada')
print(name)

#####################

name = 'global string'


def greetings():
    # name='Cinar'

    def hello():
        # name = 'Ada'
        print('hello ' + name)

    hello()


greetings()

#########################################

# x = 50
#
#
# def test(x):
#     print(f'x {x}')
#
#     x = 100
#     print(f'changed x to {x}')
#
# test(x)
# print(x)

#############################################

x = 50


def test():
    global x
    print(f'x {x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)




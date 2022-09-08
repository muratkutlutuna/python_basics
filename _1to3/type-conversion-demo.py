'''
    circle field        : pi r ** 2
    perimeter of circle : 2 pi r

    * Yari capi verilen bir dairenin alan ve cevresini hesaplayiniz. (r:3.14)
'''

radius = float(input("radius of the circle: "))
pi = 3.14
field = pi*(radius**2)
perimeter = 2 * pi * radius
print('field =',field)
print('perimeter =',perimeter)
print("field = "+str(field)+", perimeter = "+str(perimeter))



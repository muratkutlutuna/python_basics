# generators create us a iterator which don't use any memory

# def cube():
#     # result = []
#     for i in range(5):
#         yield i**3
#         # result.append(i**3)
#     # return result
#
# generator = cube()
#
# iterator = iter(generator)
# # print(cube())
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



# def cube():
#     # result = []
#     for i in range(5):
#         yield i**3
#         # result.append(i**3)
#     # return result
#
# iterator = cube()
#
# # print(cube())
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



# def cube():
#     for i in range(5):
#         yield i**3
#
# iterator = cube()
#
# for i in iterator:
#     print(i)



# def cube():
#     for i in range(5):
#         yield i**3
#
# for i in cube():
#     print(i)




liste = [i ** 3 for i in range(5)] # list
print(liste)

generator = (i ** 3 for i in range(5)) # generator, which doesn't use space in memory

print(generator)

for i in generator:
    print(i)
    
# print(next(generator))
# print(next(generator))
# print(next(generator))

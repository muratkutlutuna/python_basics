# list = [1,2,3]
#
# for item in list:
#     print(item)

# for item in range(50,100,10):
#     print(item)
#
# print(list(range(50,100,20)))
#enumerate
# greetings = 'hello there'
# for item in enumerate(greetings):
#     print(item)
# index = 0
# for index,letter in enumerate(greetings):
    # print(f'index: {index},letter:{letter}')
    # index+=1

list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]
print(list(zip(list1, list2,list3)))
for item in zip(list1,list2,list3):
    print(item)
for a,b,c in zip(list1,list2,list3):
    print(a,b,c)

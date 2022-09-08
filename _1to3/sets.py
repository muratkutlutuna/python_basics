fruits = {'orange','apple','banana'}
# print(fruits[0]) indexlenemez
for x in fruits:
    print(x)
fruits.add('cherry')
print(fruits)
fruits.update(['mango','grape','apple']) # apple zaten oldugu icin duplicate olmaz
print(fruits)

fruits.remove('mango')
fruits.discard('apple')
fruits.pop() # normalde listte son elemani siliyordu ama suan neyi silecegini bilemeyiz
fruits.clear()
print(fruits)

# myList=[1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))

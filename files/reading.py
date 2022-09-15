# try:
#     file = open("newfile3.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatasi")
# finally:
#     print("dosya kapandi")
#     file.close()


file = open("newfile.txt","r",encoding="utf-16")

# for dongusu

# for i in file:
#     print(i, end="")

#***************  read() fonksiyonu

# content1 = file.read()
# print("icerik 1")
# print(content1)
#
# # file = open("newfile.txt","r",encoding="utf-16")
# content2 = file.read()
# print("icerik 2")
# print(content2)
# file.close()


# content = file.read(5)
# content = file.read(3)
# content = file.read(3)
# print(content)
# file.close()


#********** readline() fonksiyonu

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),)
# print(file.readline(),)
# print(file.readline(),)

#********** readlines() fonksiyonu

liste = file.readlines()
print(liste)
print(liste[0])
print(liste[1])
print(liste[2])
file.close()



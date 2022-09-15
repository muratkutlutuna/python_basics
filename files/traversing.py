# file = open("newfile.txt", "r", encoding="utf-8")
# content = file.read()
# print(content)
# file.close()


# with open("newfile.txt", "r", encoding="utf-16") as file:
#     content = file.read()
#     print(content)
#     file.seek(0)
#     print(file.tell())
#     content2 = file.read()
#     print(content2)


# with open("newfile.txt", "r", encoding="utf-16") as file:
#     content = file.read()
#     print(content)
#     file.seek(10)
#     print(file.tell())
#     content2 = file.read()
#     print(content2)


with open("newfile.txt", "r", encoding="utf-16") as file:
    content = file.read(10)
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read(10)
    print(content2)



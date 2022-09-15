# with open("newfile.txt", "r+", encoding="utf-16") as file:
#     file.seek(20)
#     print(file.write("deneme"))
#
# with open("newfile.txt","r+",encoding="utf-16") as file:
#     print(file.read())


# ******* sayfa sonunda guncelleme

# with open("newfile.txt","a",encoding="utf-16") as file:
#     file.write("\nEmel Turan")

# ******* sayfa basinda guncelleme

# with open("newfile.txt","r+",encoding="utf-16") as file:
#     content = file.read()
#     content = "Efe Turan\n"+content
#     file.seek(0)
#     file.write(content)


# ******* sayfa ortasinda guncelleme

# with open("newfile.txt","r+",encoding="utf-16") as file:
#     list = file.readlines()
#     # help(list.insert)
#     list.insert(0,"Ali Korkmaz\n")
#     file.seek(0)
#     for i in list:
#         file.write(i)
#     print(list)
#
# with open("newfile.txt","r",encoding="utf-16") as file:
#     print(file.read())

with open("newfile.txt","r+",encoding="utf-16") as file:
    list = file.readlines()
    # help(list.insert)
    list.insert(0,"Yilmaz Aygun\n")
    file.seek(0)
    file.writelines(list)
    print(list)

with open("newfile.txt","r",encoding="utf-16") as file:
    print(file.read())


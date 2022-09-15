# Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir.
# Kullanimi: open(dosya_adi,dosya_eridme_modu)
# dosya_erisme_modu => dosyayi hangi amacla actigimizi belirtir.

# "W": (Write) yazma modu. Dosyayi konumda olusturur.
# file = open("newfile.txt", "w") #<_io.TextIOWrapper name='newfile.txt' mode='w' encoding='UTF-8'>
# file = open("/home/user/Desktop/newFile.py","w") #<_io.TextIOWrapper name='/home/user/Desktop/newFile.py' mode='w' encoding='UTF-8'>

# file.close()
# file = open("newfile.txt", "w",encoding='utf-16')
# file.write("sadik turan")
# file.close()

# "a": (Append) ekleme. Dosya konumda yoksa olusturur.

# file = open("newfile.txt", "a",encoding='utf-16')
# file.write("\nCinar Turan")
# file.write("Cinar Turan\n")
# file.close()

# "x": (Create) olusturma. Dosya zaten varsa hata verir. FileExistsError: [Errno 17] File exists: 'newfile2.txt'

# file = open("newfile2.txt", "x",encoding='utf-16')

# "r": (Read) okuma. varsayilan. dosya konumda yoksa hata verir.
# x = 10
#
# if x > 5:
#     raise Exception("x 5 ten buyuk deger alamaz")


# def check_password(psw):
#     import re # regular expressions
#     if len(psw)<8:
#         raise Exception("parola en az 7 karakter olmalidir.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("parola kucuk harf icermelidir")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("parola buyuk harf icermelidir")
#     elif not re.search("[0-9]", psw):
#         raise Exception("parola rakam icermelidir")
#     elif not re.search("[_@$]", psw):
#         raise Exception("parola alpha numeric karakter icermelidir")
#     elif re.search("[\s]", psw):
#         raise Exception("parola bosluk icermelidir")
#     else:
#         print("gecerli parola")
# password = "123456"
#
# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("gecerli parola: else")
# finally:
#     print("validation tamamlandi")


class Person:
    def __init__(self, name, year):
        if len(name)>10:
            raise Exception("name alani fazla karakter iceriyor.")
        else:
            self.name = name

p = Person("Aliiiiiiiiiiiiiiiiii",1989)
print(p)


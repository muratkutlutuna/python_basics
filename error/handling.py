# error handling => hata yonetimi

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('y icin 0 girilmez')
# except ValueError:
#     print('Lutfen sayi giriniz')


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('yanlis bilgi girdiniz')
#     print(e)


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except BaseException as e:
#     print('yanlis bilgi girdiniz')
#     print(e)


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('yanlis bilgi girdiniz')
# else:
#     print('hersey yolunda')

# while True:
#     try:
#         x = int(input('x: '))
#         y = int(input('y: '))
#         print(x/y)
#     except:
#         print('yanlis bilgi girdiniz')
#     else:
#         break


while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('yanlis bilgi girdiniz', ex)
    else:
        break
    finally:
        print('tty except sonlandi')
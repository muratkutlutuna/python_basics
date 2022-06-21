website = "https://www.sadikturan.com"
course = "Python Kursu: Bastan sona python programlama rehberiniz (40 saat)"
# 1- 'course' karakter dizisinde kac karakter bulunmaktadir?
lengthCourse = len(course)
print(lengthCourse)
# 2- 'website' icinden www karakterlerini alin
print(website[8:11])
# 3- 'website' icinden com karakterlerini alin
print(website[len(website)-3:len(website)])
print(website[23:26])
# 4- 'course' icinden ilk 15 ve son 15 karakterlerini alin
print("first 15 = "+course[0:15]+", last 15 = "+course[len(course)-15:len(course)])
print(course[:15])
print(course[-15:])
# 5- 'course' ifadesindeki karakterleri terten yazdirin
print(course[::])
print(course[::1])
print(course[::-1])
s = '12345'*5
print(s)
print(s[::5])
name, surname, age, job = 'Bora', 'Yilmaz', 32, 'muhendis'

# 6- Yukarida verilen degiskenler ile ejrana asagidaki ifsadeyi yazdirin
#    'Benim adim Bora Yilmaz, Yasim 32 ve meslegim muhanedis.'
result = "Benim adim "+name+" "+surname+ ", Yasim "+str(age)+" ve meslegim "+job
result = 'Benim adim {} {}, Yasim {} ve meslegim {}.' .format(name,surname,age,job)
result = f'Benim adim {name} {surname}, Yasim {age} ve meslegim {job}.'
print(result)
# 7- 'Hello world' ifadesindeki w harfini 'W' ile degistirin
str = 'Hello world'
print(str[6])
s = str[0:6]+'W'+str[7:]
s = str[0:6]+'W'+str[-4:]
str.replace('w','W')
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdirin.
result = 'abc'*3
print(result)

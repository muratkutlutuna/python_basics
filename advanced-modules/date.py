# import datetime
#
# result = dir(datetime)
# """
# classes inside the datetime module
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__', '
# date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta',
# 'timezone', 'tzinfo']
# """
# print(result)



from datetime import datetime
# from datetime import date
# from datetime import time
# result = dir(time)
# result = dir(date)

# result = dir(datetime)
# print(result)

simdi = datetime.now()
result = simdi.year #2022
result = simdi.month #9
print(result)
result = simdi.day #17
print(result)
result = simdi.hour #20
print(result)
result = simdi.minute #36
print(result)
result = simdi.second #51
print(result)
result = datetime.ctime(simdi) # Sat Sep 17 20:38:15 2022
print(result)
result = datetime.strftime(simdi,'%Y')
print("Y: "+result)
result = datetime.strftime(simdi,'%y')
print("y: "+result)
result = datetime.strftime(simdi,'%X')
print("X: "+result)
result = datetime.strftime(simdi,'%x')
print("x: "+result)
result = datetime.strftime(simdi,'%D')
print("D: "+result)
result = datetime.strftime(simdi,'%d')
print("d: "+result)
result = datetime.strftime(simdi,'%A')
print("A: "+result)
result = datetime.strftime(simdi,'%a')
print("a: "+result)
result = datetime.strftime(simdi,'%B')
print("B: "+result)
result = datetime.strftime(simdi,'%b')
print("b: "+result)
'''
Y: 2022
y: 22
X: 21:12:36
x: 09/17/22
D: 09/17/22
d: 17
A: Saturday
a: Sat
B: September
b: Sep
'''
print()


# t = '21 April 2019'
# gun, ay ,yil = t.split()
# print(gun)
# print(ay)
# print(yil)



# t = '15 April 2019 hour 10:12:30'
# dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
# result=dt.year
# print(result)



birthday = datetime(1983,3,7,12,30,10)
print(birthday)
timestamp = datetime.timestamp(birthday) # second type
print(f'timestamp: {timestamp}') #timestamp: 415884610.0
fromtimestamp = datetime.fromtimestamp(timestamp)
print(f'fromtimestamp: {fromtimestamp}') #fromtimestamp: 1983-03-07 12:30:10 second to datetime
result = datetime.fromtimestamp(0)
print(f'milad: {result}')#milad: 1970-01-01 01:00:00 bilgisayarlar icin kullanilan baslangic
                            # tarihi budur

result = simdi - birthday #timedelta
print(result)

# result = result.days()
# print(result)
# result = result.seconds()
# print(result)
# result = result.microseconds()
# print(result)



from datetime import timedelta
print()
print(simdi)
result = simdi + timedelta(days=10)
print(result)
result = simdi + timedelta(days=730, minutes=10)
print(result)
result = simdi - timedelta(days=730, minutes=10)
print(result)








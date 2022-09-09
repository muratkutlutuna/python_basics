mylist = [1,2,3]
myString = 'my string'

print(len(mylist))
print(len(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi olusturuluyor')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print('movie is deleted!')

m = Movie('film adi', 'yonetmen', 'filmin suresi')


print(type(m))
# print(len(m))

print(mylist)
print(m)

print(str(mylist))
print(str(m))

print(m.__del__())
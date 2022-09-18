import simplejson as json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # Load users frpm .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding="utf-8") as f:
                users = json.load(f)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('Kullanici olusturuldu')

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapildi')
                break
    def loggedOut(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('cikis yapild.')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('giris yapilmadi')

    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json', 'w') as f:
            json.dump(list,f)  # burda json user diye bir classi kabul etmiyor o sebeple belki bu class i bir dicte cevirmeliyiz


repository = UserRepository()

while True:
    print('Menu'.center(50, '*'))
    secim = input('1- Register\n2- Login\n3-Logout\n4- identity\n5- Exit\n seciminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('Username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password=password, email=email)
            repository.register(user)
            print(repository)
        elif secim == '2':
            if repository.isLoggedIn:
                print('zaten giris yapilmis')
            else:
                username = input('Username: ')
                password = input('password: ')
                repository.login(username,password)
        elif secim == '3':
            repository.loggedOut()
        elif secim == '4':
            repository.identity()
        else:
            print("Ynalis secim")

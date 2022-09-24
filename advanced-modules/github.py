import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'
        self.headers = {
            'Authorization': 'Bearer '+self.token,
            'Content-Type': 'application/json'
        }

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepository(self, name):
        response = requests.post(self.api_url+"/user/repos",json={
            # "authorization":self.token,
            "name":name,
            "description":"This is your first repository",
            "homepage":"https://muratkutlutuna.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        },headers=self.headers)
        return response.json()

github = Github()

while True:
    secim = input('1- Find User\n2- Get Repository\n3- Create Repository\n4 - Exit\nSecim: ')

    if secim == 4:
        break
    else:
        if secim =='1':
            username =input('username')
            result = github.getUser(username)
            print(f'name: {result["name"]} public repos: {result["public_repos"]} follower: {result["followers"]}')
        elif secim == '2':
            username =input('username')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        elif secim == '4':
            break
        else:
            print('Yanlis secim')
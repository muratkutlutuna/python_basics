# themoviedb.org => film ve dizi arsivi
# themoviedb'nin sundugu apiyi uygulamanizda kullaniniz.
# Anahtar kelimeye gore arama
# En populer film listesi
# Vizyondaki film listesi

import requests
import json

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "831cf44bc9a77fcccfc66f1013e79337"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self,keyword,page):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page={page}")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2-Search movies\n3-Exit=\nSecim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])
        if secim == "2":
            try:
                keyword = input("lutfen anahtar kelimeyi giriniz")
                page = input("Lutfen sonuclarin kac sayfa girilmesi gerektigini giriniz")
                movies = movieApi.getSearchResults(keyword, page)
                for movie in movies["results"]:
                    print(f'name {movie["name"]} with id {movie["id"]}')
            except BaseException as ex:
                print(movies.text)
                print(ex)









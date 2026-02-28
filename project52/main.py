from bs4 import BeautifulSoup
import requests


URL="https://www.timeout.com/film/best-movies-of-all-time"

response=requests.get(URL)
web_page=response.text
soup=BeautifulSoup(web_page,"html.parser")


all_movies=soup.find_all(name="h3",class_="_h3_137z8_1")
movie_titles=[movie.getText() for movie in all_movies]
movies=movie_titles[::-1]

with open("C:/Users/CASPER/Desktop/python_projects/project52/movies.txt",mode="w",encoding="utf-8") as file:
    for movie in movies:
        movie_cleaned=movie.replace("�","")
        file.write(f"{movie_cleaned}\n")

    


    
  









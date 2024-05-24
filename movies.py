from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://moviesjoy.is/movie"
link=requests.get(url)
soup=BeautifulSoup(link.content,'lxml')
movies=soup.find_all('div' ,class_="flw-item")
list=[]
for movie in movies:
    name=movie.find('h2',class_="film-name").text
    year=movie.find('span',class_="fdi-item").text
    list.append({
        "Name":name,
        "Year":year
    })
df=pd.DataFrame(list)
df.to_excel("C:\\Users\\Admin\\Webscraping\\movies.xlsx" ,index=False)
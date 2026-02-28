from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/news")
yc_web_page=response.text
soup=BeautifulSoup(yc_web_page,"html.parser")

print(soup.title)  # To see title
print(soup.title.string)  # to see title's string section


# Just for find a specific thing
article_tag=soup.find(name="span",class_="titleline")
article_text=article_tag.getText()
article_link=article_tag.find(name="a")
article_upvote=soup.find(name="span",class_="score").getText()




# For find all of them
articles=soup.find_all(name="a",class_="storylink")
article_texts=[]
article_links=[]
for article_tag in articles:
    article_text=article_tag.getText()
    article_texts.append(article_text)
    article_link=article_tag.get("href")
    article_links.append(article_link)
    
# article_upvotes= [score.getText() for score in soup.find_all(name="span",class_="score").getText()]


print(article_texts)
print(article_links)
# print(article_upvotes)
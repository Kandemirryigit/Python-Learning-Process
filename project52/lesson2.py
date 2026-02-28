from bs4 import BeautifulSoup

with open("C:/Users/CASPER/Desktop/python_projects/project52/website.html") as file:
    contents=file.read()


soup=BeautifulSoup(contents,"html.parser")



all_a=soup.find_all(name="a")  # Finds all a tags
all_p=soup.find_all(name="p")  # finds all p tags
all_img=soup.find_all(name="img")


# To get all texts inside p 
for tag in all_p:
    print(tag.getText())


# To get all href inside a
for tag in all_a:
    print(tag.get("href"))


# to get all src inside img
for tag in all_img:
    print(tag.get("src"))


# Just going to give me this specific id
img=soup.find(name="img",id="img1")
print(img)


# Just going to give me this specific thing not all h3
h3=soup.find(name="h3",class_="firsth3")
print(h3)

# the differencebetween select and select_one is select_one is going to give first item
id=soup.select_one(selector="#img1")
print(id)

# Also usable this class version
class1=soup.select(".firsth3")
print(class1)
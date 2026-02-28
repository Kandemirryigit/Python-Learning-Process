from bs4 import BeautifulSoup  # To use these things we should import this


# To read file
with open("C:/Users/CASPER/Desktop/python_projects/project52/website.html") as file:
    contents=file.read()
    

# If html.parser doesn't work you can import lxml and you can also use that 
soup=BeautifulSoup(contents,"html.parser") 



title=soup.title  # to see title
title_name=soup.title.name
title_string=soup.title.string

print(title)
print(title_name)
print(title_string)


h1=soup.h1   # This is gonna give me first h1
h1_name=soup.h1.name
h1_string=soup.h1.string


print(h1)  
print(h1_name)
print(h1_string)


print(soup)  # Not indente
print(soup.prettify())  # Indente much more readable


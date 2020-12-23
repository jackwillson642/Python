from bs4 import BeautifulSoup as bs
#  import requests

with open('test.html') as html_file:
    soup = bs(html_file, 'lxml')

#  # To print the entire html file
#  print(soup.prettify())
#
#  # To find particular tags
#  match = soup.title.text
#  print(match)
#
#  # More on finding
#  match2 = soup.find('div', class_='footer').text
#  print(match2)


### Getting all searh engines
for search_engine in soup.find_all('div', class_='search'):
    #  print(search_engine)

    name = search_engine.h2.a.text
    print(name)

    description = search_engine.p.text
    print(description)

    print()

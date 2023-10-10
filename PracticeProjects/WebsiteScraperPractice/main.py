import requests
from bs4 import BeautifulSoup as bs

# Making a get request
r = requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')

# Parsing the HTML
soup = bs(r.content, 'html.parser')

################################

# Printing the Title for fun
print(soup.title)

# Finding the div with class name 'text', this is called the id
s = soup.find('div', class_='text')

# Getting all the content between <p></p> within the id above^^
content = s.find_all('p')

# Showing the content
for line in content:
    print(line.text)

#################################


# Another Example but doing the unordered list (ul) of sidebars on the left

# Have to find under what div ID the list is under
left = soup.find('div', id = 'home-page')

# Finding the unordered list in this div
leftBar = left.find('ul', class_="leftBarList")

# Finding all elements in the unordered list ('li')
content = leftBar.find_all('li')

# printing all the leftbars material 

for line in content:
    print(line.text)


##############################################


images_list = []
images = soup.select('img')

for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({'src':src, 'alt':alt})

for image in images_list:
    print (image)

##############################################

URL = ['https://www.geeksforgeeks.org', 'https://www.geeksforgeeks.org/page/10/']

for url in range(0, 2):
    req = requests.get(URL[url])
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('div', attrs={'class', 'head'})
    for i in range(0, min(19, len(titles))):
        if url + 1 > 1:
            print(f"{(i - 3) + url * 15}" + titles[i].text)
        else:
            print(f"{i - 3}" + titles[i].text)

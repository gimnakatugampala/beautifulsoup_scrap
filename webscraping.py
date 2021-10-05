from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="section-1">
        <h3 data-hello="hi">Hello</h3>
        <img src="https://source.unsplash.com/random" >
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora dolorem eius odio numquam harum, quas architecto sit, dicta assumenda, atque earum! Temporibus saepe harum quae sapiente cupiditate distinctio culpa quasi!</p>
    </div>

    <div id="section-2">
        <ul class="items">
            <li class="item"><a href="#">item 1</a></li>
            <li class="item"><a href="#">item 2</a></li>
            <li class="item"><a href="#">item 3</a></li>
            <li class="item"><a href="#">item 4</a></li>
            <li class="item"><a href="#">item 5</a></li>
        </ul>
    </div>
    
</body>
</html>

"""

soup = BeautifulSoup(html_doc,'html.parser')

# # Direct
# print(soup.body)
# print(soup.head)
# print(soup.head.title)

# # find()
# el = soup.find('div')


# find_all() or findAll()
# el = soup.find_all('div')
# el = soup.find_all('div')[1]

# Get based on classes & Ids
# el = soup.find(id='section-1')
# el = soup.find(class_='items')
# el = soup.find(attrs={"data-hello":"hi"})

# # Select
# el = soup.select('#section-1')
# el = soup.select('#section-1')[0]
# el = soup.select('.item')[0]

# #get_text()
# el = soup.find(class_='item').get_text()

#Loop through items
# for item in soup.select('.item'):
#     print(item.get_text())
    
#Navigation
# el = soup.body.contents[1].contents[1].find_next_sibling()
# el = soup.find(id='section-2').find_previous_sibling()
# el = soup.find(class_='item').find_parent()
el = soup.find('h3').find_next_sibling('p')


print(el)
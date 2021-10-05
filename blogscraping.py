import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://webscraper.io/blog')

soup = BeautifulSoup(response.text,'html.parser')

posts = soup.find_all(class_='col-md-8')

with open('posts.csv','w') as csv_file:
     csv_writer = writer(csv_file)
     headers = ['Title','Link','Date']
     csv_writer.writerow(headers)

     for post in posts:
        title = post.find(class_='titleblog').get_text()
        link = post.find('a')['href']
        date = post.select('.date')[0].get_text()
        csv_writer.writerow([title,link,date])
        
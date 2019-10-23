from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('insert URL here').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('inset file name here', 'a')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Material'])

for article in soup.find_all('a', class_='name'):
    name = article.text
    print(name)
    csv_writer.writerow([name])

csv_file.close()


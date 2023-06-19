import requests
import csv
from bs4 import BeautifulSoup
from random import randint
from time import sleep


file = open('notebook.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['ლეპტოპის დასახელება' , 'ფასი'])

page_number = 1
while page_number <= 5:
    url = f'https://alta.ge/notebooks-page-{page_number}.html?features_hash=329-4933'
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    notebook = soup.find('div', class_='grid-list')
    all_notebook = notebook.find_all('div', class_='ty-column3')
    page_number+=1

    for notebook in all_notebook:
        name = notebook.find('a', class_='product-title')
        price = notebook.find('span', class_='ty-price-num')
        csv_obj.writerow([name.text , price.text])

sleep(randint(10,25))
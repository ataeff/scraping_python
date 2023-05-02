
"""" 
Scrap the following websites, save to csv file:
https://futurepedia.io 
https://aitoolsdirectory.com/ 
https://www.insidr.ai/ai-tools/ 
https://dataloop.ai/blog/ai-generated-tools-for-every-need-full-list/ 
https://allthingsai.com/
https://topai.tools/lists/ai-newsletter-list.html
https://theresanaiforthat.com/

"""""


from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
import time
import requests
import json


out = {}

def futurepedia_parse():
    for count in range(1, 189):
        url = f"https://www.futurepedia.io/api/tools?page={count}&sort=verified"
        response = requests.get(url).text
        obj = json.loads(response)

        for i in obj:
            name = i['toolName']
            link = i['websiteUrl']
            out[name] = link
        time.sleep(1)
    return out


def aiToolsDirectory_parse():
    url = 'https://aitoolsdirectory.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    news_elements = driver.find_elements(By.CLASS_NAME, 'sv-tile__body')
    for element in news_elements:
        time.sleep(3)
        link_element = element.find_element(By.CLASS_NAME, 'sv-link-reset')
        name_element = link_element.find_element(By.TAG_NAME, 'h3').text
        out[name_element] = link_element.get_attribute('href')
    return out


def dataLoop_parse():
    url = 'https://dataloop.ai/blog/ai-generated-tools-for-every-need-full-list/'
    response = requests.get(url).text
    bs = BeautifulSoup(response, 'lxml', exclude_encodings='utf-8')

    elem = bs.find_all('a', 'in-cell-link')
    for i in elem:
        name = i.get_text()
        link = i.get('href')
        out[name] = link
    return out


def allThingsAI_parse():
    url = 'https://allthingsai.com/'
    response = requests.get(url).text
    bs = BeautifulSoup(response, 'lxml', exclude_encodings='utf-8')

    elem = bs.find_all('a', 'framer-1ygrvdy framer-9rk99h')
    for i in elem:
        name = i.find('h3', 'framer-text framer-styles-preset-12lj5ox').get_text()
        link = i.get('href')
        link_end = url + link[2:]
        out[name] = link_end
    return out


def topAiTools_parse():
    url = 'https://topai.tools/lists/ai-newsletter-list.html'
    response = requests.get(url).text
    bs = BeautifulSoup(response, 'lxml', exclude_encodings='utf-8')

    elem = bs.find_all('h5', 'mt-3 mb-2')
    for i in elem:
        name = str(i.contents[0]).strip()[3:]
        link = i.find('a').get('href')
        out[name] = link
    return out


def theresAnAiForThat_parse():
    url = 'https://theresanaiforthat.com/'
    response = requests.get(url).text
    bs = BeautifulSoup(response, 'lxml', exclude_encodings='utf-8')

    elem = bs.find_all('div', 'ai_link_wrap')
    for i in elem:
        name = i.find('a', 'ai_link new_tab c_event').get_text()
        link = i.find('a', 'external_ai_link').get('href')
        out[name] = link
    return out



def save_to_csv():
    with open('scraping.csv', 'w', encoding='utf-8', newline='') as file:
        field_names = ['NAME', 'LINK']
        writer = csv.DictWriter(file, fieldnames=field_names, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for name, values in out.items():
            writer.writerow(dict(NAME=name, LINK=values))




# ---------------------------------------
"""For Remove the duplicates"""

# class Parse:
#     def __init__(self, name, link):
#         self.name = name
#         self.link = link
#
#
# out = {}
# with open('scraping.csv', 'r', encoding='utf-8') as file:
#     reader_obj = csv.DictReader(file)
#     for item in reader_obj:
#         name = str(item['NAME']).strip().lower()
#         p1 = Parse(str(item['NAME']).strip(), item['LINK'])    # out = {'name': 'p1'(key: value)}, передаем объект чтобы сохранить оригинальное имя
#         out[name] = p1
#
# print(out)


# with open('scrapingNEW.csv', 'w', encoding='utf-8', newline='') as file:
#     field_names = ['NAME', 'LINK']
#     writer = csv.DictWriter(file, fieldnames=field_names, quoting=csv.QUOTE_ALL)
#     writer.writeheader()
#     for name, values in out.items():
#         writer.writerow(dict(NAME=values.name, LINK=values.link))  # key = p1(key)  values = p1(value)

#


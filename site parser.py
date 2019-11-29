import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


def get_html(url):
    response = requests.get(url)
    return response.text


# def data_list(html):
#     soup = BeautifulSoup(html, 'lxml')
#     try:
#         names = soup.find('id', class_='no-wrap currency-name').find_all('data-sort')
#     except:
#         # print(Exception(soup.find('td', class_='no-wrap currency-name').get('data-sort')))
#         names = 'null'
#     return names


def data_of_data(html):
    # soup = BeautifulSoup(html, 'lxml')
    names = re.findall(r'''class="no-wrap currency-name" data-sort="(.+)"''', html)
    price = re.findall(r'''class="price" data-usd="(.+)" ''', html)
    # print(len(names))
    # print(len(price))
    # try:
    #     names = soup.find('id', class_='no-wrap currency-name').find_all('data-sort')
    # except:
    #     # print(Exception(soup.find('td', class_='no-wrap currency-name').get('data-sort')))
    #     names = 'null'
    datas = {}
    for j in range(len(names)):
        datas[names[j]] = str(price[j])
    return datas


def csv_write(datas):
    with open('result', encoding='utf-8', mode='w+')as f:
        for i in datas:
            f.write('name: ' + i + '\nprice: ' + datas[i] + '\n')


def main():
    start = datetime.now()
    url = 'https://coinmarketcap.com/all/views/all'
    csv_write(data_of_data(get_html(url)))
    end = datetime.now()
    print(end - start)


if __name__ == '__main__':
    main()
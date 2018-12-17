import requests
from bs4 import BeautifulSoup
import time
import html2text
import random
import ware_house

name_txt = 'duphaston_3_1'
web_page = 'https://irecommend.ru/content/gormonalnye-preparaty-solvay-pharma-dyufaston?page='

desktop_agents = ware_house.desktop_agents


def replace_other(text):
    """This function replace all not necessary symbols in the text"""
    for i in ware_house.replace_list:
        text = text.replace(i, "")

    return (text)


def random_headers():
    """This function create a random header for my parser"""
    return {'User-Agent': random.choice(desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def handle_text(text):
    """This function handle text and make it in the good format"""
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.escape_all = True
    text = h.handle(text)
    text = replace_other(text)
    return (text)


def request_action(url, timeout):
    r = requests.get(url, headers=random_headers(), timeout=timeout)
    soup = BeautifulSoup(r.text, 'html.parser')
    return (soup)









for j in range(2, 7):
    url = web_page + str(j)
    soup = request_action(url, 20)
    spans = soup.find_all('a', attrs={'class': "more"})
    websites = []
    for span in spans:
        websites.append(span.attrs['href'])

    for i in range(len(websites)):
        text = ''
        url = 'https://irecommend.ru' + str(websites[i])  # % (user_id) # url для второй страницы
        soup = request_action(url, 20)
        spans = soup.find_all('div', attrs={'class': "description hasinlineimage"})
        text = url + str(spans)

        time.sleep(random.randint(10, 30))

        while text[((str(text).find("!["))):((str(text).find("g)"))) + 2]:
            text = text.replace(text[((str(text).find("!["))):((str(text).find("g)"))) + 2], '')

        if (i % 6 == 0) and (i != 0):
            print("""Time to sleep, :) , i = """, i)
            time.sleep(30)

    text = handle_text(text)

    my_file = open(name_txt + '.txt', 'a', encoding='utf-16')
    my_file.write(text)
    my_file.close()
    print("""It's cool""")
    time.sleep(20)

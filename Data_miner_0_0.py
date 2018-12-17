import requests
from bs4 import BeautifulSoup
import time
import html2text
user_id = 12345



headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
url = 'https://irecommend.ru/content/gepatoprotektor-hospira-geptral' #% (user_id) # url для второй страницы
r = requests.get(url, headers,    timeout=10)
soup = BeautifulSoup(r.text, 'html.parser')


spans = soup.find_all('a', attrs = {'class':"more"}) #, attrs={'id':'titleDescriptionID'}

websites = []
for span in spans:
    websites.append(span.attrs['href'])
    print (span.attrs['href'])


all_info = ''
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}
for i in range(len(websites)):

    url = 'https://irecommend.ru' + str(websites[i])  # % (user_id) # url для второй страницы
    r = requests.get(url, headers=headers, timeout=60)
    soup = BeautifulSoup(r.text, 'html.parser')
    spans = soup.find_all('div', attrs={'class': "description hasinlineimage"})
    text = str(spans)
    all_info = all_info + text

#     text = all_info
#     while text[((str(text).find("!["))):((str(text).find("g)"))) + 2]:
#         text = text.replace(text[((str(text).find("!["))):((str(text).find("g)"))) + 2], '')
    if (i % 6 == 0) and (i != 0):

        time.sleep(1800)
#
# h = html2text.HTML2Text()
# h.ignore_links = True
# h.escape_all = True
# text = h.handle(text)
# text = text.replace(".", "")
# text = text.replace(",", "")
# text = text.replace(":", "")
# text = text.replace(";", "")
# text = text.replace("\"", "")
# text = text.replace("!", "")
# text = text.replace("â€œ", "")
# text = text.replace("â€˜", "")
# text = text.replace("*", "")
# text = text.replace(">", "")
# text = text.replace("—", "")
# text = text.replace("""[""", "")
# text = text.replace("]", "")
# text = text.replace("_", "")
# text = text.replace("+", "")
# text = text.replace("-", "")
# text = text.replace("✔", "")
# f = open('text.txt', 'w')
# for index in text:
#     f.write(str(index).encode('utf8'))
# f.close()
#

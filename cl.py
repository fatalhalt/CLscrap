import argparse
import sys
import requests
from bs4 import BeautifulSoup


def query_craigslist(baseurl=None, keyword='wrx|sti'):
    if baseurl is None:
        baseurl = 'https://chicago.craigslist.org'
    response = requests.get(baseurl + '/search/pta', params={'query': keyword, 'srchType': 'T'})
    soup = BeautifulSoup(response.content, "html.parser")

    results = soup.find_all('li', {'class': 'result-row'})  # at max 120 results per 1 page
    items = []

    for i in results:
        try:
            title = i.find('a', {'class': 'result-title hdrlnk'}).get_text()
            link = i.find('a', {'class': 'result-title hdrlnk'}).get('href')
            date = i.find('time', {'class': 'result-date'}).get('datetime')
            price = i.find('span', {'class': 'result-price'}).get_text()
            hood = i.find('span', {'class': 'result-hood'}).get_text()
            imgs = i.find('a', {'class': 'result-image gallery'}).get('data-ids').split(',')
            img_1 = 'https://images.craigslist.org/' + imgs[0][2:] + '_300x300.jpg'
            d = {'title': title, 'link': link, 'date': date, 'price': price, 'hood': hood, 'img': img_1}
            items.append(d)
        except AttributeError:
            pass  # ignore empty fields

    return items, baseurl, keyword


def main():
    parser = argparse.ArgumentParser(description="craigslist WRX and STi parts finder", parents=())
    parser.add_argument("-b", "--baseurl", help='baseurl, e.g. https://chicago.craigslist.org')
    parser.add_argument("-k", "--keyword", default='wrx|sti', help='keyword to search')

    args, extra_args = parser.parse_known_args()
    partlist = query_craigslist(args.baseurl, args.keyword)
    print(partlist)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

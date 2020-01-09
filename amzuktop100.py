import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def top100UK():
    for i in range(3):
        url = "https://www.amazon.co.uk/Best-Sellers-Electronics-Mobile-Phone-Cases-Covers/zgbs/electronics/340321031/ref=zg_bs_pg_1?_encoding=UTF8&pg={}".format(
            i)
        r = requests.get(url)
        soup = BeautifulSoup(r.content)

        try:
            top100 = soup.find('div', {'id': 'zg-center-div'}).find_all('span', {'class': 'a-list-item'})
            for top100item in top100:
                top100title = str(top100item.find('div', {'aria-hidden': 'true'}).text.strip())

                # top100price = str(top100item.find('span', {'class': 'p13n-sc-price'}).text)

                top100ranking = str(top100item.find('span', {'class': 'zg-badge-text'}).text)

                # top100asin = str(top100item.find('a').get('href'))

                # Review Date 를 불러온다.
                # tmpReviewDate = reviewItem.find('span', {'data-hook': 'review-date'}).text.split()
                # reviewDate = tmpReviewDate[1] + " " + tmpReviewDate[2] + " " + tmpReviewDate[3]

                # Review Body 를 불러온다.
                # reviewBody = str(reviewItem.find('span', {'data-hook': 'review-body'}).text)

                # reviewCount = reviewItem.find('span', {'class': 'review-comment-total aok-hidden'}).text

                # print(top100ranking + " : " + top100title + " : " + top100asin.split('/')[3])
                print(top100ranking + " : " + top100title.split(' ')[0] + " : " + top100title)
                # print(top100title.split())

        except:
            print("ERROR")


def main():
    top100UK()


if __name__ == "__main__":
    main()

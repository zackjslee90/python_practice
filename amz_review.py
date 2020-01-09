import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getReviews():
    testASIN = input("Type ASIN: ")
    for i in range(1, 30):
        reviewURL = "https://www.amazon.co.uk/product-review/product-reviews/" + testASIN + "/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={}".format(
            i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
        }
        page = requests.get(reviewURL, headers=headers, verify=False)
        pageHTML = page.text

        pageSource = BeautifulSoup(pageHTML, "lxml")

        try:
            reviewGroup = pageSource.find('div', {'id': 'cm_cr-review_list'}).find_all('div', {'data-hook': 'review'})
            for reviewItem in reviewGroup:
                # Review ID 를 불러온다.
                reviewID = str(reviewItem.get('id'))

                # Rating은 [ N out of 5 stars ] 중 첫번째 배열만 검출한다.
                reviewRating = str(reviewItem.find('i', {'data-hook': 'review-star-rating'}).text.split()[0])

                # Review Title 을 불러온다.
                reviewTitle = str(reviewItem.find('a', {'data-hook': 'review-title'}).text)

                # Review Author 를 불러온다.
                reviewAuthor = str(reviewItem.find('span', {'class': 'a-profile-name'}).text)

                # Review Date 를 불러온다.
                # tmpReviewDate = reviewItem.find('span', {'data-hook': 'review-date'}).text.split()
                # reviewDate = tmpReviewDate[1] + " " + tmpReviewDate[2] + " " + tmpReviewDate[3]

                # Review Body 를 불러온다.
                reviewBody = str(reviewItem.find('span', {'data-hook': 'review-body'}).text)

                # print(reviewID)
                # print(reviewAuthor)
                # print(reviewRating + reviewTitle)
                # print(reviewBody)

                print("ID : " + reviewAuthor + " | Rating : " + reviewRating + " | Title : " + reviewTitle + " | Content : " + reviewBody + " | URL :" + "https://www.amazon.co.uk/gp/customer-reviews/" + reviewID + "\n")

        except:
            print("ERROR")


def main():
    getReviews()


if __name__ == "__main__":
    main()

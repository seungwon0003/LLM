import time
from selenium import webdriver
from bs4 import BeautifulSoup

def crawl_yanolja_reviews(name, url):
    review_list = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    scroll_count = 3
    for i in range(scroll_count):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
    soup = BeautifulSoup(driver.page_source)
    
    review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div')
    review_date = soup.select(review_date = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p'))

    for i in range(len(review_containers)):

        # print(i)
        review_text = review_containers[i].find('p', class_='content-text').text
        date = review_date[i].text
        
        review_empty_stars = review_containers[i].find_all('path', {'fill-rule':'evenodd'})
        stars = 5 - len(review_empty_stars)

        review_dict = {
            'review':review_text,
            'star':stars,
            'date':date
        }
        review_list.append(review_dict)
    print(review_list)
    time.sleep(10)

crawl_yanolja_reviews('라발스 호텔 부산', 'https://nol.yanolja.com/reviews/domestic/3020201')
import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://media.dlib.indiana.edu/catalog?f%5Bcollection_ssim%5D%5B%5D=Clio+Awards&per_page=100&page='


def scrape(url, lc):
    # GET req to URL
    response = requests.get(url)
    line_count = lc
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_='blacklight-abstract_ssi col-sm-9')

    # line_count = sum(1 for line in open('scraped_content.txt', encoding="utf8"))

    with open('scraped_content_copy.txt', 'a', encoding='utf-8') as file:
        # Write the content of each element to the text file
        for i, element in enumerate(elements, start=line_count):
            file.write(str(i)+" "+ element.text + '\n')
            line_count += 1

line_count = 1
for i in range(1, 19):
    line_count = (i-1)*100 + 1
    scrape(url+str(i), line_count)
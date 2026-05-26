#import requests
#from bs4 import BeautifulSoup


#headers = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
#}

#def Extract(url):
#    response = requests.get(url, headers=headers).content
#    soup = BeautifulSoup(response, "html.parser")
#    tag = soup.find('h2')
#    print(tag)





#Extract(url = "https://en.wikipedia.org/wiki/Main_Page")




import requests
from bs4 import BeautifulSoup
import csv


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

def Extract(url):
    response = requests.get(url, headers=headers).content
    soup = BeautifulSoup(response, "html.parser")

    tag = soup.find('td', {'id': 'mp-right'})

    content = [span.text for span in tag.find_all('span')]

    with open("wiki.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(content)




Extract(url = "https://en.wikipedia.org/wiki/Main_Page")



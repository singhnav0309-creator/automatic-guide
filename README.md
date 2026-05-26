## IMPLEMENTATION OF WEB SCRAPING

# I done a assignment based on web scraping using 'requests' and 'beautifulsoup'

## Softwares used
  - Python
  - Pycharm
  - Visual Studio
  
## Features 
  - Send requests to website
  - Parse HTML pages
  - Extract specific HTML elements i.e. 'id', 'div', etc...
  - Beginner friendly project structure
  - Works with Wikipedia and static websites i.e. Google, etc...
 
## Project Structure
  - Web Scraping/
    |
    |- web.py
    |- web02.py
    |- web03.py
       |- wiki.csv
    |- web04.py
       |- eagle
    |- web05.py
    |- README.md

## Installation
  - pip install requests
  - pip install beautifulsoup
  - pip install lxml

## HOW TO RUN
  - Clone the repository https://github.com/singhnav0309-creator/automatic-guide.git

  - Go to any of file

  - run in a terminal

## Example code
   
    import requests
    from bs4 import BeautifulSoup


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
        }

    def Extract(url):
    response = requests.get(url, headers=headers).content
    soup = BeautifulSoup(response, "html.parser")
    tag = soup.find('h2')
    print(tag)

Extract(url = "https://en.wikipedia.org/wiki/Main_Page")

# run this python file
 - python web03.py

## NOTES
 - Some websites blocks scraping.
 - Selenium is required for working on Dynamic websites.
 - Website HTML structure can change anytime.

## AUTHOR
- Navjot Singh



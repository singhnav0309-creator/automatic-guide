import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/Dell-Wireless-Keyboard-Mouse-Spill-Resistant/dp/B09T3H12GV?pf_rd_p=ad288fb5-635e-41bc-b0c0-ae88c875ce98&pf_rd_r=AA6HCG1JXDRZ95MBEZP6&ref_=AUG-LapsUNrec_B09T3H12GV"

user_agent = {
    "User_Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

def product_title():
    title = self.soup.find("span",{"id": "producttitle"}).text

    if title is not None:
        return title.text.strip()

    else:
        return "tag not found"


def product_price():
    price = self.soup.find("span",{"id": "priceblock_ourprice"})

    if price is not None:
        return price.text.strip()
    else:
        return "not available"


class Price_Tracer:
    def __init__(self):
        self.url = url
        self.user_agent = "{user_agent}:"
        self.response = requests.get(self.url, headers=self.user_agent)
        self.soup = BeautifulSoup(self.response.content, "html.parser")

device=Price_Tracer



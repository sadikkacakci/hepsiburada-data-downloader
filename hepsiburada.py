import requests
from bs4 import BeautifulSoup
import pandas as pd

class HepsiBurada:
    def __init__(self,keyword):
        self.keyword = keyword
        self.headers = {"User-Agent":""}

    def getLinks(self):
        url = f"https://www.hepsiburada.com/ara?q={self.keyword}"
        response = requests.get(url,headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")
        list = soup.find("ul",{"class":"productListContent-frGrtf5XrVXRwJ05HUfU productListContent-rEYj2_8SETJUeqNhyzSm"}).find_all("li")
        links = []
        for row in list:
            text = row.find("a",href=True)
            if text==None:
                continue
            links.append(text["href"])
        return links

    def getPrices(self):
        dictionary = {}
        liste = []
        links = self.getLinks()
        for link in links:
            all_link = "https://www.hepsiburada.com"
            if link[0:4] == "http":
                all_link = link
            else:
                all_link = all_link + link
            response = requests.get(all_link,headers=self.headers)
            soup = BeautifulSoup(response.text, "html.parser")
            span = soup.find("span",attrs={"data-bind":"markupText:'currentPriceBeforePoint'"})
            h1 = soup.find("h1",attrs={"class":"product-name best-price-trick"})
            dictionary.update({h1.text.strip():span.text})
            liste.append([h1.text.strip(),span.text])
        return liste

    def toDataFrame(self):
        dict = self.getPrices()
        df = pd.DataFrame(data = dict)
        df.columns = ["ürün","fiyat"]
        return df

    def writeExcel(self):
        df = self.toDataFrame()
        df.to_excel(f"output/{self.keyword}.xlsx", index=False)

    def writeCsv(self):
        df = self.toDataFrame()
        df.to_csv(f"output/{self.keyword}.csv", index= False)
    
    def writeTxt(self):
        df = self.toDataFrame()
        df.to_csv(f"output/{self.keyword}.txt",sep = " ", header=False, index=False)
        

def processing(keyword):
    keyword = keyword.replace(" ", "+")
    return keyword
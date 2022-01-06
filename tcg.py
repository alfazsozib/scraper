from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

def  web_driver():
    return webdriver.Chrome(executable_path='D:/chromedriver_96/chromedriver.exe')

def data_collect():
    box = soup.find_all(
        'section',{'class':'search-result__product'})
    all_data = []
    for i in box:
        cat = ''
        title = ''
        price = ''
        try:
            cat = i.find(
                'section',{'class':'search-result__rarity'}).text
        except:
            cat = 'None'
        try:    
            title = i.find(
                'span',{'class':'search-result__title'}).text
        except:
            title = 'None'
        try:    
            price = i.find(
                'span',{'class':'search-result__market-price--value'}).text
        except:
            price = 'None'

        data_dict ={

            'Category':cat,
            'Title':title,
            'Price':price
        } 
        all_data.append(data_dict)
        df = pd.DataFrame(all_data)
        df.to_csv('tcgplayer.csv') 
        print('----Running----')
         
    df = pd.DataFrame(all_data)
    df.to_csv('tcgplayer.csv')    
    print('Scraping Complete')    
    driver.close()      


if __name__ =='__main__':
    driver = web_driver()
    url = 'https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&q=Ash%20Blossom&view=grid'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,features='lxml')
    time.sleep(3)
    data_collect()
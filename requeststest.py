import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver

#payload = {'name' : 'Stephen Chou', 'email' : 'sccusr@gmail.com'}
#sup = requests.get('https://www.supremenewyork.com/checkout', data=payload)
#sup = requests.get("https://www.supremenewyork.com/all")
# print(help(sup))

#with open('sup.html', 'wb') as f:
 #   f.write(sup.content)

#print(sup.headers)

#chrome = webdriver.Chrome('/Users/stephenchou/Desktop/PersonalProjects/Resources/selenium/chromedriver')
#chrome.get("https://www.supremenewyork.com/checkout")


def get_item_id(stock, keyword):

        for key, items in stock['products_and_categories'].items():
                if key == 'Sweatshirts':
                        for i in range(len(items)):
                                x = re.search(keyword, items[i]['name'])
                                if (x):
                                        itemID = items[i]['id']
                                        return(itemID)





def get_size_color_id(styles_webpage, color, size):
        styles_dict = styles_webpage['styles']
        for colors in range(len(styles_dict)):
                if styles_dict[colors]['name'] == color:
                        color_id = styles_dict[colors]['id']
                        for sizes in range(len(styles_dict[colors]['sizes'])):
                                if styles_dict[colors]['sizes'][sizes]['name'] == size:
                                        size_id = styles_dict[colors]['sizes'][sizes]['id']
        return color_id, size_id


# url = "https://www.supremenewyork.com/mobile_stock.json"
# stock = requests.get(url).json()

# keyword = 'Cutout Logo'
# itemID = get_item_id(stock, keyword)
#
#
# styles_webpage = requests.get("https://www.supremenewyork.com/shop/{}.json".format(itemID)).json()
# color = 'Natural'
# size = 'Large'
#
# color_id, size_id = get_size_color_id(styles_webpage, color, size)

# Getting droplist from SupremeCommunity
# droplist_site= requests.get('https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-04-30/')
# droplist_html = BeautifulSoup(droplist_site.text, 'html.parser')
# print(droplist_html.prettify())
item = BeautifulSoup('<h2 class="name item-details item-details-title">Cutout Logo Crewneck</h2>', 'html.parser')
item_tag = item.h2
print(item_tag['class'])
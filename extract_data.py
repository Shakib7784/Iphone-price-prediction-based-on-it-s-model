import requests as r;
from bs4 import BeautifulSoup
import re
import csv
url = "https://en.wikipedia.org/wiki/IPhone"
data = r.get(url).text
soup = BeautifulSoup(data,'html5lib')
table = soup.find('table', class_= 'wikitable')
rows = table.find_all('tr')[2:] # we want to skip first 2 row that is why we have started from row 2 to end
data_dict = {}
for row in rows:
    data = row.find_all(['th','td'])
    # againdata = data[0].find_all('a')# if we want to get the name from a tag we won't get from it. 
    try:
        version_text=data[0].a.text.split(' ')[1] # we have to use this method. we are keeping this line inside try because some of row don't have a tag
        version_number = re.findall(r'\d+',version_text)[0]
        version_number = int (version_number)
        # print(version_number)
        price_text = data[-1].text.split('/')[-1].replace("$"," ") # data[-1] means last column
        price_number = re.findall(r'\d+', price_text)[0]
        price_number=int(price_number)
        if(price_number>100):
            data_dict[version_number]=price_number
            # print(version_number,price_number)
    except:
        pass 


# for key, value in data_dict.items():
#     print(key , value)
fields = ["product", "price"]
with open("phonedata.csv",'w', newline='') as csvfile:
    csvwrite = csv.writer(csvfile)
    csvwrite.writerow(fields)
    for item,value in data_dict.items():
        csvwrite.writerow([item,value])
    # for data in data_dict:
    #     csvwrite.writerow([data,data_dict[data]])


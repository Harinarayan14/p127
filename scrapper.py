from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(start_url)
print(page)

soup = bs(page.text,'html.parser')

stars_table = soup.find('table')

temp_list= []
table_rows = stars_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star = []
distance =[]
mass = []
radius =[]
luminosity = []

for i in range(1,len(temp_list)):
    star.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    luminosity.append(temp_list[i][7])
    
df = pd.DataFrame(list(zip(star,distance,mass,radius,luminosity)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df)

df.to_csv('bright_stars.csv')

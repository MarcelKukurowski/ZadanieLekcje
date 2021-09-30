import requests
from bs4 import BeautifulSoup
import pprint
import datetime as dt

username = "ckziu"
password = "zseis"
days_of_the_week = ['Niedziela','Poniedziałek','Wtorek','Środa','Czwartek','Piątek','Sobota']
lesson_hour = [80000,85000,94000,103000,113000,122000,131000,140000,144500]
list_counter = 0
now = dt.datetime.now()
current_time = now.strftime('%H:%M:%S')
#current_time = str(dt.time(8,00))
current_date = int(now.strftime('%w'))
current_day_of_week = days_of_the_week[current_date]
current_lesson = ''
next_lesson = ''
key_list = []
key2_list = []
first_key = '8:00- 8:45'

days = {}

r = requests.get(f'https://{username}:{password}@zseis.zgora.pl/plan/plany/o9.html')

page_content = r.text

soup = BeautifulSoup(page_content, 'html.parser')

table = soup.find('table', attrs={'class': 'tabela'})

rows = table.find_all('tr')

i = 0
for row in rows:
    
    if(i == 0):
        cols = row.find_all('th')
        cols = [ele.text.strip() for ele in cols[2:]]
        for ele in cols:
            days[ele] = {}
        i+=1
        continue

    cols2 = row.find_all('td')
    cols2 = [ele2.text.strip() for ele2 in cols2[1:]]
    
    days["Poniedziałek"][cols2[0]] = cols2[1]
    days["Wtorek"][cols2[0]] = cols2[2]
    days["Środa"][cols2[0]] = cols2[3]
    days["Czwartek"][cols2[0]] = cols2[4]
    days["Piątek"][cols2[0]] = cols2[5]

print("\n")

                

# Code for checking actual and next lesson

for character in [' ',':']:
    if character in current_time:
        current_time_int = current_time.replace(character,"")

current_time_int = int(current_time_int)

for index2, key in enumerate(days):
    if key == current_day_of_week:
        for index,hour in enumerate(days[key]):
            if current_time_int < lesson_hour[0] or current_time_int >= lesson_hour[list_counter] and current_time_int < lesson_hour[list_counter+1]:
                current_lesson = days[key][hour]
                #next_lesson = days[key][hour]
                key_list = list(days[key])
                value = key_list[index + 1]
                next_lesson = days[key][value]
            elif current_time_int > lesson_hour[8]:
                current_lesson = 'Koniec lekcji na dziś'
                key2_list = list(days)
                value2 = key2_list[index2 + 1]
                next_lesson = days[value2][first_key]
            list_counter += 1


 

print(f"Aktualny dzień: {current_day_of_week}")
print(f"Aktualna godzina: {current_time}")
print(f"Aktualna lekcja: {current_lesson}")
print(f"Następna lekcja: {next_lesson}")
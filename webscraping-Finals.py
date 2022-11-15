import csv
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

url = 'https://registrar.web.baylor.edu/exams-grading/fall-2022-final-exam-schedule'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers= headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

tables = soup.findAll('table')

finals_table = tables[1]

#print(finals_table)

all_rows = finals_table.findAll('tr')

myclasses_file = open('classes.csv', 'r')
myclasses = csv.reader(myclasses_file, delimiter=',')

for rec in myclasses:
    day= rec[0]
    time= rec[1]

for row in all_rows:
    cell = row.findAll('td')
    if cell:
        sch_day = cell[0].text
        sch_time = cell[1].text
        sch_exam_day = cell[2].text
        sch_exam_time = cell[3].text

        if sch_day ==day and sch_time == time:
            print(f'Class Day and Time: {day} - {time}')
            print(f'Exam Day and Time: {sch_exam_day} - {sch_exam_time}')
            print()
            print()

from bs4 import BeautifulSoup
from collections import Counter
import datetime


with open('html_text.txt', 'r', encoding='UTF-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

print(soup.prettify())


tag_dictionary = Counter([i.name for i in soup.find_all(True)])


filename = datetime.datetime.now().strftime('%d_%m_%YT%H_%M_%S_%f')

with open(filename, 'w', encoding='UTF-8') as result_file:
    result_file.write(str(dict(tag_dictionary)))


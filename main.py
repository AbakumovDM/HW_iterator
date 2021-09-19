import requests
import re

HOST_WIKI = 'https://en.wikipedia.org/wiki/'
HOST_JSON = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"

# Быстрый вариант

# country_list = []
# response = requests.get(HOST_JSON)
# for item in response.json():
#   country_name = item['name']['common']
#   country_list.append(country_name)
#
# with open("country-links.txt", "w", encoding='utf8') as file:
#   for country in country_list:
#     file.write(f'{country} - {HOST_WIKI}{country.replace(" ", "_")}\n')


class WikiCountries:
  def __init__(self, host):
    self.host = host
    self.cursor = None

  def __iter__(self):
    self.cursor = 0
    return self

  def __next__(self):
    if self.cursor == len(requests.get(self.host).json()):
      raise StopIteration
    country_name = requests.get(self.host).json()[self.cursor]['name']['common']
    self.cursor += 1
    return f'{country_name} - https://en.wikipedia.org/wiki/{country_name.replace(" ", "_")}\n'

with open("country-links2.txt", "w", encoding='utf8') as file:
  for item in WikiCountries(HOST_JSON):
    file.write(item)

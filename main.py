import pprint
import requests
"""
class Internet:
    def __init__(self):
        self.url = "Unknow"

    def get_url(self, url):
        self.url = url


class Hh(Internet):
    pass

"""
#TODO:Переработать код ниже в класс
url = "https://api.hh.ru/vacancies/"
params = {'address':'Набережные Челны',

          'page':1
          }
result = requests.get(url,params=params)
pprint.pprint(result.json()['items'][:6])


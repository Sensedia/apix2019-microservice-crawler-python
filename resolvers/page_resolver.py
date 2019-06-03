import requests
from bs4 import BeautifulSoup
from resolvers.url_resolver import url_resolve

def get_page(host, resource, kit, specification):
    resource = url_resolve(url=resource, gender=kit['gender'], type=specification['type'], color=specification['color'])
    page = requests.get(host + resource)
    return BeautifulSoup(page.text, 'html.parser') 

def get_value(*elements):
    for element in elements:
        if element is None:
            continue
        return element.get_text()
    return None

def parse_price(value):
    parsed = value.upper() \
                  .replace('R$', '') \
                  .replace(' ', '') \
                  .replace(',', '.')
    return float(parsed)

def resolve_link(prefix, text):
    if text is None:
        return text
    index = text.index(prefix)
    return text[index:len(text)]
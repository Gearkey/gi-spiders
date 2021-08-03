from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib.request
import re

def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/74.0'
    }
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    
    return response.read().decode('utf-8')

def find_it(content, tag_name, find_type, find_name):
    bs = BeautifulSoup(content, 'html.parser')
    if find_type == 'id': return str(bs.find(tag_name, id=find_name))
    if find_type == 'class': return str(bs.find(tag_name, class_=find_name))

def copy_file(from_path, to_path):
    urllib.request.urlretrieve(from_path, to_path)

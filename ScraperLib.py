import pickle
import sys
import requests
from bs4 import BeautifulSoup

sys.setrecursionlimit(10 ** 6)


def save_objects_to_path(obj, filename):
    with open(filename, "wb") as f:
        pickle.dump(len(obj), f)
        for value in obj:
            pickle.dump(value, f)


def load_objects_from_path(filename):
    data2 = []
    with open(filename, "rb") as f:
        for _ in range(pickle.load(f)):
            data2.append(pickle.load(f))
    return data2


def findElmt(soup_, html: str, identifier: str = None, id_content: str = None, get_item: str = None, get_text: bool = False, recursive: bool = True):
    temp_soup: BeautifulSoup
    if identifier is None:
        temp_soup = soup_.find(html, recursive=recursive)
    else:
        temp_soup = soup_.find(html, attrs={identifier: id_content}, recursive=recursive)
    if get_item is not None:
        return temp_soup[get_item]
    elif get_text is True:
        return temp_soup.get_text().strip()
    return temp_soup


def findAllElmt(soup_, html: str, identifier: str = None, id_content: str = None, get_item: str = None, get_text: bool = False, recursive: bool = True):
    temp_soup: list[BeautifulSoup]
    temp_txt_list: list[str] = []
    if identifier is None:
        temp_soup = soup_.find_all(html, recursive=recursive)
    else:
        temp_soup = soup_.find_all(html, attrs={identifier: id_content}, recursive=recursive)
    if get_item is not None:
        for i in temp_soup:
            temp_txt_list.append(i[get_item])
        return temp_txt_list
    elif get_text is True:
        for i in temp_soup:
            temp_txt_list.append(i.get_text().strip())
        return temp_txt_list
    return temp_soup


def requestSoup(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def removeDupFromList(x):
  return list(dict.fromkeys(x))
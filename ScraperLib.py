import pickle
import sys
import requests
from bs4 import BeautifulSoup
import os

sys.setrecursionlimit(10 ** 6)
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def ANSI_RESET(text):
    return f"\u001B[0m{text}\u001B[0m"


def ANSI_BLACK(text):
    return f"\u001B[30m{text}\u001B[0m"


def ANSI_RED(text):
    return f"\u001B[31m{text}\u001B[0m"


def ANSI_GREEN(text):
    return f"\u001B[32m{text}\u001B[0m"


def ANSI_YELLOW(text):
    return f"\u001B[33m{text}\u001B[0m"


def ANSI_BLUE(text):
    return f"\u001B[34m{text}\u001B[0m"


def ANSI_PURPLE(text):
    return f"\u001B[35m{text}\u001B[0m"


def ANSI_CYAN(text):
    return f"\u001B[36m{text}\u001B[0m"


def ANSI_WHITE(text):
    return f"\u001B[37m{text}\u001B[0m"


def ANSI_RAINBOW(text):
    i = 0
    rainbow_str: str = ''
    for char in text:
        if char == ' ':
            rainbow_str += ' '
        elif i == 0:
            rainbow_str += ANSI_RED(char)
            i += 1
        elif i == 1:
            rainbow_str += ANSI_YELLOW(char)
            i += 1
        elif i == 2:
            rainbow_str += ANSI_GREEN(char)
            i += 1
        elif i == 3:
            rainbow_str += ANSI_BLUE(char)
            i += 1
        else:
            rainbow_str += ANSI_PURPLE(char)
            i = 0
    return rainbow_str


# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def read_textfile(filename):
    lines=[]
    with open (filename, encoding='utf8') as f:
        lines = f.readlines()
    return lines




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


def findElmt(soup_, html: str, identifier: str = None, id_content: str = None, get_item: str = None,
             get_text: bool = False, recursive: bool = True):
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


def findAllElmt(soup_, html: str, identifier: str = None, id_content: str = None, get_item: str = None,
                get_text: bool = False, recursive: bool = True):
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


class ProgressBar:
    process_count = 0
    process_length = 0
    process_pretext = ''

    @classmethod
    def start(cls):
        cls.process_count = 0
        clearConsole()
        print(cls.process_pretext, end='')
        for i in range(cls.process_length):
            print(ANSI_RED('_'), end='')

    @classmethod
    def update(cls):
        cls.process_count += 1
        clearConsole()
        print(cls.process_pretext, end='')
        for i in range(cls.process_count):
            print(ANSI_GREEN('='), end='')
        for i in range(cls.process_length - cls.process_count):
            print(ANSI_RED('_'), end='')

import pickle
import sys
from enum import Enum

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


ansi_rainbow_global_variable: int = 0


def ANSI_RAINBOW(text, reset_on=0):
    global ansi_rainbow_global_variable
    if reset_on is 0 or ansi_rainbow_global_variable % reset_on == 0:
        ansi_rainbow_global_variable = 0
    rainbow_str: str = ''
    for char in text:
        if char == ' ':
            rainbow_str += ' '
        elif ansi_rainbow_global_variable == 0:
            rainbow_str += ANSI_RED(char)
            ansi_rainbow_global_variable += 1
        elif ansi_rainbow_global_variable == 1:
            rainbow_str += ANSI_YELLOW(char)
            ansi_rainbow_global_variable += 1
        elif ansi_rainbow_global_variable == 2:
            rainbow_str += ANSI_GREEN(char)
            ansi_rainbow_global_variable += 1
        elif ansi_rainbow_global_variable == 3:
            rainbow_str += ANSI_BLUE(char)
            ansi_rainbow_global_variable += 1
        else:
            rainbow_str += ANSI_PURPLE(char)
            ansi_rainbow_global_variable = 0
    return rainbow_str


# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


def read_textfile(filename):
    lines = []
    with open(filename, encoding='utf8') as f:
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


# ProgressBar.new_bar('th', len(list[object]), 'pre-fix', )

# ProgressBar.update('th')

# ProgressBar.start('th', 'st')

class BarDesign(Enum):
    simple = 0
    nyan_cat = 1


class ProgressBar:
    def __init__(self, tag: str, length: int = 0, pre_fix: str = '', bar_design: BarDesign = 1,
                 display_time_elapsed: bool = False, is_relative: bool = True):
        self.progress: int = 0
        self.tag: str = tag
        self.length: int = length
        self.pre_fix: str = pre_fix
        self.design: BarDesign = bar_design
        self.time_elapsed: bool = display_time_elapsed
        self.is_relative: bool = is_relative


class Loading:
    progress_bars: list[ProgressBar] = []
    active_progress_bars: list[ProgressBar] = []

    @classmethod
    def start(cls, *args):
        for arg in args:
            for bar in cls.progress_bars:
                if bar.tag == arg:
                    cls.active_progress_bars.append(bar)
        clearConsole()
        cls.print_active_bars()

    @classmethod
    def update(cls, tag: str):
        for bar in cls.active_progress_bars:
            if bar.tag == tag:
                bar.progress += 1
        else:
            clearConsole()
            cls.print_active_bars()

    @classmethod
    def removeActive(cls):
        for prg in cls.active_progress_bars:
            cls.progress_bars.remove(prg)
        cls.active_progress_bars = []

    @staticmethod
    def print_nyancat(model: ProgressBar):
        nyancat = read_textfile('nyanloadingbar.txt')
        print('')
        for no in nyancat:
            print(model.progress * ANSI_RAINBOW('#', reset_on=len(nyancat)), no, end='')

    @classmethod
    def print_active_bars(cls):
        for bar in cls.active_progress_bars:
            if bar.design == 0:
                pass
                # something to create a simple
            elif bar.design == 1:
                cls.print_nyancat(bar)
        print('')

    @classmethod
    def new_bar(cls, tag: str, length: int = 0, pre_fix='', bar_design: BarDesign = 1,
                display_time_elapsed: bool = False, is_relative: bool = True):
        bar = ProgressBar(tag, length, pre_fix, bar_design, display_time_elapsed, is_relative)
        cls.progress_bars.append(bar)

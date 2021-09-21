import pickle
import sys
import time
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


def ANSI_RAINBOW(text, reset_on=10):
    global ansi_rainbow_global_variable
    if reset_on == 0 or ansi_rainbow_global_variable % reset_on == 0:
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


def remove_dubs_heavy(_list):
    new_list = []
    seen = [] # set()  # set for fast O(1) amortized lookup
    for line in _list:
        if line.price == 0:
            continue
        if (line.name + str(line.product_number)) in seen:
            # line.print()
            continue  # skip duplicate
        seen.append(line.name + str(line.product_number))
        new_list.append(line)
        # line.print()
    # print('removed lines:', len(_list) - len(new_list), 'new_list len:', len(new_list))
    return new_list


def numbersToRelativeSize(length, progress, get_full_length: bool = False, size: int = 40):
    if length == 0 or progress == 0:
        return 0
    if get_full_length:
        return size - int(((progress / length) * size))
    else:
        return int((progress / length) * size)


# ProgressBar.new_bar('th', len(list[object]), 'pre-fix', )

# ProgressBar.start('th', 'st')

# ProgressBar.update('th')

class BarDesign(Enum):
    simple = 0
    nyan_cat = 1
    not_so_simple = 2


class ProgressBar:
    amount = 0

    def __init__(self, tag: str, length: int = 0, pre_fix: str = '', bar_design: BarDesign = BarDesign.not_so_simple,
                 display_time_elapsed: bool = False, is_relative: bool = True, display_percent: bool = True, ):
        self.progress: int = 0
        self.tag: str = tag
        self.length: int = length
        self.pre_fix: str = pre_fix
        self.design: BarDesign = bar_design
        self.time_elapsed: bool = display_time_elapsed
        self.is_relative: bool = is_relative
        self.display_percent: bool = display_percent
        self.start_time: time = time.time()
        self.end_time: time = time.time()
        self.add()

    @classmethod
    def add(cls):
        cls.amount += 1


class Loading:
    progress_bars: list[ProgressBar] = []
    active_progress_bars: list[ProgressBar] = []

    @classmethod
    def start(cls, *args):
        for arg in args:
            for bar in cls.progress_bars:
                if bar.tag == arg:
                    bar.start_time = time.time()
                    bar.end_time = time.time()
                    cls.active_progress_bars.append(bar)
        # clearConsole()
        # cls.print_active_bars()

    @classmethod
    def update(cls, tag: str):
        for bar in cls.active_progress_bars:
            if bar.tag == tag:
                bar.progress += 1
            if bar.length - bar.progress == 0 and bar.end_time == bar.start_time and bar.length != 0:
                bar.end_time = time.time()
            cls.print_active_bars()

    @classmethod
    def removeActive(cls):
        for prg in cls.active_progress_bars:
            cls.progress_bars.remove(prg)
        cls.active_progress_bars = []

    @classmethod
    def update_length(cls, tag: str, new_length: int):
        for bar in cls.active_progress_bars:
            if bar.tag == tag:
                bar.length = new_length
        for bar in cls.progress_bars:
            if bar.tag == tag:
                bar.length = new_length

    @staticmethod
    def print_simple_bar(model: ProgressBar):
        print(model.pre_fix.ljust(22), '>[', numbersToRelativeSize(model.length, model.progress) * ANSI_GREEN('='),
              end='')
        print(numbersToRelativeSize(model.length, model.progress, get_full_length=True) * ANSI_RED('='), ']<', end='')
        if model.display_percent and model.length != 0:
            print(' ', int((model.progress / model.length) * 100), '%', end='')
        if model.time_elapsed:
            if model.length - model.progress != 0:
                print('\n|', int(time.time() - model.start_time), 'seconds', end='')
            else:
                print('\n| finished in', int(model.end_time - model.start_time), 'seconds', end='')
        print('\n')

    @staticmethod
    def print_nyancat(model: ProgressBar):
        nyancat = read_textfile('nyanloadingbar.txt')
        print('')
        for no in nyancat:
            print(numbersToRelativeSize(model.length, model.progress) * ANSI_RAINBOW('#', reset_on=len(nyancat)), no,
                  end='')
            # print((numbersToRelativeSize(model.length, model.progress, get_full_length=True) - len(no)) * ' ', '|', end='')

    @staticmethod
    def print_not_simple_bar(model: ProgressBar):
        print(model.pre_fix.ljust(22), '>[', numbersToRelativeSize(model.length, model.progress) * ANSI_GREEN('='),
              end='')
        print(numbersToRelativeSize(model.length, model.progress, get_full_length=True) * ANSI_RED('='), ']<', end='')
        if model.display_percent and model.length != 0:
            print(' ', int((model.progress / model.length) * 100), '%', end='')
        if model.time_elapsed:
            if model.length - model.progress != 0:
                print('\n|', int(time.time() - model.start_time), 'seconds', end='')
            else:
                print('\n| finished in', int(model.end_time - model.start_time), 'seconds', end='')
        print('\n')

    @classmethod
    def print_active_bars(cls):
        clearConsole()
        for bar in cls.active_progress_bars:
            if bar.design == 0:
                cls.print_simple_bar(bar)
            elif bar.design == 1:
                cls.print_nyancat(bar)
            elif bar.design == 2:
                cls.print_not_simple_bar(bar)
            # print('\n')

    @classmethod
    def new_bar(cls, tag: str, length: int = 0, pre_fix='', bar_design: BarDesign = 2,
                display_time_elapsed: bool = True, is_relative: bool = True, display_percent: bool = True):
        bar = ProgressBar(tag, length, pre_fix, bar_design, display_time_elapsed, is_relative, display_percent)
        cls.progress_bars.append(bar)

from itertools import takewhile


class Legoset:
    def __init__(self):
        self.name: str
        self.age: int
        self.amount_bricks: int
        self.price: float
        self.product_number: int
        self.rating_amount: float
        self.rating_fun: float
        self.rating_worth: float
        # self.amount_figure: int
        self.link: str
        self.theme: str
        self.img_link: str

    def __str__(self):
        return f"{self.name} # {self.product_number}"

    def print(self):
        print(self.name[:40].ljust(43, '_'), 'age', str(self.age).ljust(2), 'brick amount',
              str(self.amount_bricks).ljust(5), 'price', str(self.price).ljust(5),
              'Stars ⭐', str(self.rating_amount).ljust(3), 'FunRating ⭐', str(self.rating_fun).ljust(3),
              'RatingWorth ⭐', str(self.rating_worth).ljust(3), 'prod nr:', str(self.product_number).ljust(14))

    @classmethod
    def print_list(cls, list_=[]):
        for set_ in list_:
            set_.print()


class Theme:
    def __init__(self):
        self.name: str
        self.link: str


# LINQ (c#) python equivalence
# http://mark-dot-net.blogspot.com/2014/03/python-equivalents-of-linq-methods.html

def take_above_price(equal_or_above: float, list_: list[Legoset]):
    sub_list = []
    for i in list_:
        if i.price >= equal_or_above:
            sub_list.append(i)
    return sub_list


def take_below_price(equal_or_above: float, list_: list[Legoset]):
    sub_list = []
    for i in list_:
        if i.price <= equal_or_above:
            sub_list.append(i)
    return sub_list


def divide_into_age_groups(list_, divide_by_arr):
    master_list = []
    sub_list = []
    for i in divide_by_arr:
        for item in list_:
            if i[0] <= item.age <= i[1]:
                sub_list.append(item)
        master_list.append(sub_list)
        sub_list = []
    return master_list

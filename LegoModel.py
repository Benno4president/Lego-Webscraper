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

    def print(self):
        print(self.name[:40].ljust(43, '_'), 'age', str(self.age).ljust(2), 'brick amount', str(self.amount_bricks).ljust(5), 'price', str(self.price).ljust(5),
              'Stars ⭐', str(self.rating_amount).ljust(3), 'FunRating ⭐', str(self.rating_fun).ljust(3), 'RatingWorth ⭐', str(self.rating_worth).ljust(3))

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

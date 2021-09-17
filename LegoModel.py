class Legoset:
    def __init__(self):
        self.price: float
        self.age: int
        self.link: str
        self.img_link: str
        self.amount_bricks: int
        #self.amount_figure: int
        self.rating_amount: float
        self.rating_fun: float
        self.rating_worth: float
        self.theme: str
        self.product_number: int
        self.name: str



    def print(self):
        print(self.name, 'age', self.age, 'brick amount', self.amount_bricks, 'price', self.price, self.product_number, 'stars', self.rating_amount,'FunRating', self.rating_fun, 'RatingWorth', self.rating_worth)




class Theme:
    def __init__(self):
        self.name: str
        self.link: str
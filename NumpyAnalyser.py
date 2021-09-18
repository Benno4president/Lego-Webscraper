class NumpyAnal:
    def __init__(self):
        self.Start = []


    def averagepricepritem(self, prices: list[float], items: list[int]):

        psum = sum(prices)
        isum = sum(items)
        return (psum/isum)

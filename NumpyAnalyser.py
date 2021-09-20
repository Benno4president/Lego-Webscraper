import pandas as pd
import pandas_profiling as pp


def html_pd_stats(dataframe):
    profile = pp.ProfileReport(dataframe)
    profile.to_file('pandas_profiling.html')


def objects_to_pandas_df(objs):
    return pd.DataFrame([t.__dict__ for t in objs])


def save_to_csv(obj: pd.DataFrame, filename):
    obj.to_csv(filename)


def load_from_csv(filename):
    return pd.read_csv(filename)


class NumpyAnal:
    def __init__(self):
        self.Start = []

    def averagepricepritem(self, prices: list[float], items: list[int]):
        psum = sum(prices)
        isum = sum(items)
        return (psum / isum)

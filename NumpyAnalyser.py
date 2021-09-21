import pandas as pd
import numpy as np
import pandas_profiling as pp
import plotly.graph_objects as go
import plotly.express as px

def html_pd_stats(dataframe, filename='pandas_profiling.html'):
    profile = pp.ProfileReport(dataframe)
    profile.to_file(filename)


def objects_to_pandas_df(objs):
    return pd.DataFrame([t.__dict__ for t in objs])


def dict_to_pandas_df(objs):
    return pd.DataFrame(objs)

def save_to_csv(obj: pd.DataFrame, filename):
    obj.to_csv(filename)


def load_from_csv(filename):
    return pd.read_csv(filename)


"""
def pie_charter(label_arr=[], value_arr=[], amount=9999):
    matplotlib.rcParams.update({'font.size': 20})

    # data to plot
    labels = []
    sizes = []
    colors = ['lightcoral', 'lightskyblue', 'lightblue', 'lightpink', 'lightgreen']

    # custom sorting for labels
    temp_obj_list = []
    for value in value_arr:
        temp_obj_list.append({'Label': label_arr[value_arr.index(value)], 'Val': value})
    temp_obj_list.sort(key=lambda x: x.get('Val'))
    for i in temp_obj_list:
        labels.append(i.get('Label'))
        sizes.append(i.get('Val'))


    # explode 1st slice
    explode = []
    for i in range(len(sizes)):
        explode.append(0)
    fig, axs = plt.subplots(figsize=(5, 5))
    plt.pie(sizes[:amount], explode=explode[:amount], labels=labels[:amount], colors=colors[:amount],
            autopct='%1.1f%%', shadow=False, startangle=90)

    plt.axis('equal')
    plt.show()
"""

def stonks_chart(df,x_axis ,y_axis, sort=False, by=''):
    by = x_axis
    _df = df
    if sort:
        _df = df.sort_values(by)
    fig = go.Figure([go.Scatter(x=_df[x_axis], y=_df[y_axis])])
    fig.show()

def scatter_chart(df, x_width, y_length, by=''):
    by = x_width
    _df = df.sort_values(by)# iris is a pandas DataFrame
    fig = px.scatter(_df, x_width, y_length)
    fig.show()

def orbital_chart(df, r_frequency, d_direction ):
   # df = px.data.wind()
    fig = px.bar_polar(df, r=r_frequency, theta=d_direction, color=r_frequency, template="plotly_dark",
                       color_discrete_sequence=px.colors.sequential.Plasma_r)
    fig.show()




class NumpyAnal:
    def __init__(self):
        self.Start = []

    def averagepricepritem(self, prices: list[float], items: list[int]):
        psum = sum(prices)
        isum = sum(items)
        return (psum / isum)

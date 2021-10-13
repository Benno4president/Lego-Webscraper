import sys
import pandas as pd
from pandas import DataFrame

import NumpyAnalyser


def stonks(df, args):
    if len(args) == 4:
        NumpyAnalyser.stonks_chart(df, args[2], args[3])
    elif len(args) == 5:
        NumpyAnalyser.stonks_chart(df, args[2], args[3], by=args[4])
    else:
        print('Syntax: file.csv chart_type x_axis y_axis ?sort_by')


def scatter(df, args):
    if len(args) == 4:
        NumpyAnalyser.scatter_chart(df, args[2], args[3])
    elif len(args) == 5:
        NumpyAnalyser.scatter_chart(df, args[2], args[3], by=args[4])
    else:
        print('Syntax: file.csv chart_type x_axis y_axis ?sort_by')


def orbital(df, args):
    if len(args) == 4:
        NumpyAnalyser.orbital_chart(df, args[2], args[3])
    else:
        print('Syntax: file.csv chart_type x_axis y_axis ?sort_by')

myDict = {
    "stonks": stonks,
    "scatter": scatter,
    "orbital": orbital
    #"pie": NumpyAnalyser.pie_charter()
}


def main():
    _args = sys.argv

    if len(_args) <= 2:
        _args = ['MathPlotterInterface.py', 'pickle.csv', 'scatter', 'price', 'amount_bricks']
    print(_args)

    _args.remove(_args[0])
    command_var = _args[1]
    df = NumpyAnalyser.load_from_csv(_args[0])

    # print(processed_args[0], processed_args[1], command_var)
    myDict.get(command_var, lambda: 'Invalid')(df, _args)


if __name__ == '__main__':
    main()

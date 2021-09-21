import sys
import pandas as pd
from pandas import DataFrame

import NumpyAnalyser


def stonks(args):
    _args = args
    df: DataFrame
    if len(_args) <= 3:
        pass
    elif _args[2] == '-csv':
        df = NumpyAnalyser.load_from_csv(args[3])
        NumpyAnalyser.stonks_chart(df, args[0], args[1])
    else:
        print('... stonks \'x-axis tag\' \'y-axis tag\' -csv \'filename.csv\'')


def p2(args):
    print('p2', args)

myDict = {
    "stonks": stonks,
    "P2": p2
    #"pie": NumpyAnalyser.pie_charter()
}


def main():
    _args = sys.argv

    if len(_args) <= 2:
        _args = ['MathPlotterIncerface.py', 'stonks', 'price', 'amount_bricks', '-csv', 'pickle.csv']

    command_var = _args[1]
    _args.remove(_args[0])
    _args.remove(_args[0])

    processed_args = []
    for arg in _args:
        if arg[0].isdigit() and ',' in arg:
            processed_args.append([int(c) for c in arg.split(',')])  # if you want ints
        elif ',' in arg:
            processed_args.append(arg.split(','))
        else:
            processed_args.append(arg)

    # print(processed_args[0], processed_args[1], command_var)
    myDict.get(command_var, lambda: 'Invalid')(processed_args)


if __name__ == '__main__':
    main()

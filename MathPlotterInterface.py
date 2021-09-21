import sys

import NumpyAnalyser


def p1(args):
    print('p1', args)


def p2(args):
    print('p2', args)

myDict = {
    "P1": p1,
    "P2": p2,
    "pie": NumpyAnalyser.pie_charter()
}


def main():
    _args = sys.argv
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

    print(processed_args[0], processed_args[1], command_var)
    myDict.get(command_var, lambda: 'Invalid')(processed_args)


if __name__ == '__main__':
    main()
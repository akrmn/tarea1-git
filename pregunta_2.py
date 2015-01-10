#!/usr/bin/env python3
from sys import argv, exit, stderr
from string import ascii_uppercase as letters

def main(words):
    pairs = [l*2 for l in letters]

    for word in words:
        for pair in pairs:
            if word.count(pair):
                pairs.remove(pair)

    for pair in pairs:
        print(pair, end=' ')
    print();

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ./pregunta_2.py <file>', file=stderr)
        exit(1)
    main(
        open(argv[1]).read().split()
    )

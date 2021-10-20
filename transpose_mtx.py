#!/usr/bin/env python3

from scipy.io import mmread, mmwrite
import sys

if __name__ == '__main__':
    mmwrite(sys.argv[2], mmread(sys.argv[1]).T)

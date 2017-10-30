#!/usr/bin/env python

from lib.core.__version__ import __version__
from lib.core.banner import banner

def main():
    print(banner(__version__).banner())

if __name__ == "__main__":
    main()

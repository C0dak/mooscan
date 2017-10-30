#!/usr/bin/env python

from lib.core.__version__ import __version__
from lib.core.banner import banner
from lib.core.ConfigHandler import ConfigHandler

def main():
    print(banner(__version__).banner())

    startup_tasks()

def startup_tasks():
    ConfigHandler()

if __name__ == "__main__":
    main()

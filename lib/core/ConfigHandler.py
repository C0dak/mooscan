import os
import yaml
import sys
from shutil import copyfile

class ConfigHandler(object):

    CONFIG_PATH = "~/.mooscan"
    CONFIG_FILE = "mooscan.conf"
    GIT_PATH = "moodle-git"

    def __init__(self):

        self.configdir = os.path.expanduser(self.CONFIG_PATH)
        self.configfile = self.configdir + '/' + self.CONFIG_FILE

        # Path to the config
        self.CreateConfigDirectory()
        self.CreateConfig()

        self.config = self.LoadConfig()

        self.CheckConfig()

    def CreateConfigDirectory(self):
        if not os.path.exists(self.configdir):
            print("Configuration directory {dir} does not exist".format(dir=self.configdir))
            os.makedirs(self.configdir)
            print("Directory Created")
        else:
            print("Directory {dir} already exists".format(dir=self.configdir))

    def CreateConfig(self):

        print("Searching for {file}".format(file=self.configfile))
        if not os.path.exists(self.configfile):
            copyfile('doc/mooscan.conf.skel', self.configfile)
            print("Config not found. Copying Default to {file}".format(file=self.configfile))

    def LoadConfig(self):
        return yaml.load(open(self.configfile,'rb').read())

    def CheckConfig(self):
        print("Yaml Data")
        print(self.config)

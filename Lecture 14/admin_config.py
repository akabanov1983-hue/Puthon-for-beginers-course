import configparser
cfg = configparser.ConfigParser()

cfg.read('configs.txt.txt')
cfg.read('configs.txt.txt')
cfg.sections()
for section in cfg.sections():
    print(section)
# -*- coding: utf-8 -*-
from tqdm import tqdm
from termcolor import colored


# Logs tqdm configuration
def ok(msg): tqdm.write(colored('OK --> ' + msg, 'green'))
def error(msg): tqdm.write(colored('ERROR --> ' + msg, 'red'))
def warn(msg): tqdm.write(colored('WARN --> ' + 'yellow'))



def printBanner():
    tqdm.write(colored('''----------------------------
╔═╗╔╦╗╔═╗   ╔╦╗╔═╗╔═╗╦  ╔═╗
╠═╣║║║║═╬╗   ║ ║ ║║ ║║  ╚═╗
╩ ╩╩ ╩╚═╝╚   ╩ ╚═╝╚═╝╩═╝╚═╝
----------------------------''', 'green'))

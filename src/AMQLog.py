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


def usage():
    print("Utilisation : ")
    print("python AMQTools.py -f <environnement_source> -t <environnement_cible> -q <queue_cible> -a postFirstMessage")
    print("")
    print("Options : ")
    print("-f <environnement_source> (--from) : Environnement source où vont être récupérés les messages JMS")
    print("-t <environnement_cible> (--to) : Environnement cible où vont être envoyés les messages JMS")
    print("-q <queue_cible> (--queue) : File MQ cible. La file MQ source sera déduite en préfixant par DLQ.")
    print("-a <action> (--action) : Environnement cible où vont être envoyés les messages JMS")
    print("---")
    print("  Actions possibles : postFirstMessage, postAllMessages, retryMessages, exportExcel (voir README.md)")
    print("  Environnements possibles : LOCALHOST, DEV, INT, VAL, QUA, PRD")
    print("  Queues possibles : Consumer.SGENGPP.VirtualTopic.TDATALEGACY, Consumer.SGENCLI.VirtualTopic.TDATAGPP")
    print("                     QGENGPP, SRECDNO, SGENGED, SRECOBL, QDATALEGACY, ALL, ...")

    print("  Exemples: python AMQTools.py -f VAL -t LOCALHOST -q QGENGPP -a postFirstMessage")
    print("            python AMQTools.py -f PRD -t DEV -q Consumer.SGENGPP.VirtualTopic.TDATALEGACY -a postAllMessages")
    print("---")
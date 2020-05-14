# -*- coding: utf-8 -*-
from tqdm import tqdm
from termcolor import colored
import src.AMQConfig as cfg


# Logs tqdm configuration
def debug(msg): 
    if cfg.LOGLEVEL == "DEBUG":
        tqdm.write(colored('[DEBUG] ' + msg, 'yellow'))

def info(msg): tqdm.write(colored('[INFO] ' + msg, 'green'))
def warn(msg): tqdm.write(colored('[WARN] ' + 'orange'))
def error(msg): tqdm.write(colored('[ERROR] ' + msg, 'red'))


def printBanner():
    tqdm.write(colored('''----------------------------
╔═╗╔╦╗╔═╗   ╔╦╗╔═╗╔═╗╦  ╔═╗
╠═╣║║║║═╬╗   ║ ║ ║║ ║║  ╚═╗
╩ ╩╩ ╩╚═╝╚   ╩ ╚═╝╚═╝╩═╝╚═╝
----------------------------''', 'green'))


def usage():
    print("""
Utilisation : 
    python AMQTools.py -f <environnement_source> -t <environnement_cible> -q <queue_cible> -a postFirstMessage

Options : 
    -f <environnement_source> (--from) : Environnement source où vont être recuperes les messages JMS
    -t <environnement_cible> (--to) : Environnement cible où vont être envoyes les messages JMS
    -q <queue_cible> (--queue) : File MQ cible et source.
    -a <action> (--action) : Environnement cible ou vont être envoyes les messages JMS
    -m <message> (--message) : Nom du fichier (avec son extension) contenant le message a envoyer 

Actions possibles : postFirstMessage, postAllMessages, postMessage, retryMessages, retryMessagesAllQueues, exportExcel (voir README.md)
Environnements possibles : LOCALHOST, DEV, INT, VAL, QUA, PRD
Queues possibles : QGENGPP.TDATALEGACY, QGENCLI.TDATASYNC,QGENGPP, SRECDNO, SGENGED, SRECOBL, QDATALEGACY, ...

Exemples: 
    python AMQTools.py -f PRD -a retryMessagesAllQueues
    python AMQTools.py -f PRD -a retryMessages -q DLQ.QGENGPP
    python AMQTools.py -f PRD -a exportExcel -q DLQ.QGENGPP
    python AMQTools.py -f VAL -t LOCALHOST -a postFirstMessage -q DLQ.QGENGPP.TDATALEGACY
    python AMQTools.py -f PRD -t DEV -a postAllMessages -q DLQ.QGENGPP.TDATALEGACY
    python AMQTools.py -f DEV -a postMessage -q DLQ.QGENCLI.TDATASYNC -m QGENCLI.TDATASYNC-Notification-CLI_ASSURE_RETRAITE.json
    """)
    
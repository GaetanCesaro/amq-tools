# -*- coding: utf-8 -*-
import sys, getopt
import src.AMQConfig as cfg
import src.AMQCore as core
import src.AMQLog as log
from tqdm import tqdm
from termcolor import colored


def usage():
    print("Utilisation : ")
    print("python AMQTools.py -f <environnement_source> -t <environnement_cible> -q <queue_cible> -a postFirstMessage")
    print("")
    print("Options : ")
    print("-o : Génère un fichier Excel contenant les messages JMS est généré")
    print("-f <environnement_source> (--from) : Environnement source où vont être récupérés les messages JMS")
    print("-t <environnement_cible> (--to) : Environnement cible où vont être envoyés les messages JMS")
    print("-q <queue_cible> (--queue) : File MQ cible. La file MQ source sera déduite en préfixant par DLQ.")
    print("-a <action> (--action) : Environnement cible où vont être envoyés les messages JMS")
    print("  Actions possibles : postFirstMessage, postAllMessages, etc...")


def main():
    #log.printBanner()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hof:t:f:q:a:", ["help", "output","from","to","queue","action"])

    except getopt.GetoptError as err:
        log.err(err)  
        usage()
        sys.exit(2)
    
    writeExcelFile = False
    srcEnv = ""
    dstEnv = ""
    srcQueue = ""
    dstQueue = ""
    action = ""

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-o", "--output"):
            writeExcelFile = True
        elif opt in ("-f", "--from"):
            srcEnv = arg
        elif opt in ("-t", "--to"):
            dstEnv = arg
        elif opt in ("-q", "--queue"):
            dstQueue = arg
            srcQueue = "DLQ."+dstQueue
        elif opt in ("-a", "--action"):
            action = arg    
        else:
            assert False, "unhandled option"

    # Paramètres obligatoires sinon on sort
    if not srcEnv or not dstEnv or not dstQueue:
        usage()
        sys.exit()

    print("FROM ENV", srcEnv, "--> TO", dstEnv)
    SRC_ENV = cfg.ENVIRONNEMENTS[srcEnv]
    DST_ENV = cfg.ENVIRONNEMENTS[dstEnv]

    print("FROM QUEUE", srcQueue, "--> TO", dstQueue)
    SRC_QUEUE = srcQueue
    DST_QUEUE = dstQueue

    allMessages = core.getAllMessages(SRC_ENV, SRC_QUEUE)
    bodyList = core.formatMessages(allMessages, SRC_ENV, DST_QUEUE, writeExcelFile)

    # Post d'un seul message
    if action == "postFirstMessage":            
        if (bodyList[0] is not None):
            log.ok("Posting first message from queue %s to queue %s" %(SRC_QUEUE, DST_QUEUE))
            core.postMessage(DST_ENV, DST_QUEUE, bodyList[0])
        else:
            log.warn("Nothing to post")

    # Post de tous les messages
    if action == "postAllMessages":
        log.ok("Posting all messages from queue %s to queue %s" %(SRC_QUEUE, DST_QUEUE))
        for message in tqdm(bodyList):
            core.postMessage(DST_ENV, DST_QUEUE, message)


if __name__ == "__main__":
    main()

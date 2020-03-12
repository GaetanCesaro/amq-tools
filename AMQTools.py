# -*- coding: utf-8 -*-
import sys, getopt, json, os
import src.AMQConfig as cfg
import src.AMQCore as core
import src.AMQLog as log
from tqdm import tqdm
from termcolor import colored


def checkParameters(action, srcEnv, dstEnv, dstQueue):
    # Paramètres obligatoires sinon on sort
    if action == "retryMessagesAllQueues" or action == "postMessage":
        if not srcEnv:
            log.error("L'environnement source est obligatoire")  
            log.usage()
            sys.exit()
    elif action == "retryMessages" or action == "exportExcel":
        if not srcEnv or not dstQueue:
            log.error("L'environnement source et la queue de destination sont obligatoires")  
            log.usage()
            sys.exit()  
    else:
        if not srcEnv or not dstEnv or not dstQueue:
            log.error("L'environnement source, l'environnement cible et la queue de destination sont obligatoires")  
            log.usage()
            sys.exit()


def main():
    #log.printBanner()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:t:f:q:a:m:", ["help","from","to","queue","action","filename"])

    except getopt.GetoptError as err:
        log.error(str(err))  
        log.usage()
        sys.exit(2)
    
    writeExcelFile = False
    srcEnv = ""
    dstEnv = ""
    srcQueue = ""
    dstQueue = ""
    action = ""
    filename = ""

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            log.usage()
            sys.exit()
        elif opt in ("-f", "--from"):
            srcEnv = arg
        elif opt in ("-t", "--to"):
            dstEnv = arg
        elif opt in ("-q", "--queue"):
            dstQueue = arg
            srcQueue = "DLQ."+dstQueue
        elif opt in ("-a", "--action"):
            action = arg
        elif opt in ("-m", "--message"):
            filename = arg
        else:
            assert False, "unhandled option"

    checkParameters(action, srcEnv, dstEnv, dstQueue)

    SRC_ENV = cfg.ENVIRONNEMENTS[srcEnv]
    if dstEnv:
        print("FROM ENV", srcEnv, "--> TO", dstEnv)
        DST_ENV = cfg.ENVIRONNEMENTS[dstEnv]
    else:
        print("FROM ENV", srcEnv)

    if srcQueue:
        print("FROM QUEUE", srcQueue, "--> TO", dstQueue)
        SRC_QUEUE = srcQueue
        DST_QUEUE = dstQueue

    # Export Excel des messages de la DLQ
    if action == "exportExcel":
        log.info("Génération du fichier Excel")
        writeExcelFile = True

        allMessages = core.getAllMessages(SRC_ENV, SRC_QUEUE)
        bodyList = core.formatMessages(allMessages, SRC_ENV, DST_QUEUE, writeExcelFile)

    # Post d'un seul message
    if action == "postFirstMessage":            
        log.info("Post 1er message de queue %s vers queue %s" %(SRC_QUEUE, DST_QUEUE))

        allMessages = core.getAllMessages(SRC_ENV, SRC_QUEUE)
        bodyList = core.formatMessages(allMessages, SRC_ENV, DST_QUEUE, writeExcelFile)

        if (bodyList[0] is not None):
            core.postMessage(DST_ENV, DST_QUEUE, bodyList[0])
        else:
            log.warn("Nothing to post")

    # Post de tous les messages
    if action == "postAllMessages":
        log.info("Posting all messages from queue %s to queue %s" %(SRC_QUEUE, DST_QUEUE))

        allMessages = core.getAllMessages(SRC_ENV, SRC_QUEUE)
        bodyList = core.formatMessages(allMessages, SRC_ENV, DST_QUEUE, writeExcelFile)
        
        for message in tqdm(bodyList):
            core.postMessage(DST_ENV, DST_QUEUE, message)

    # Retry des messages
    if action == "retryMessages":
        core.retryMessages(SRC_ENV, SRC_QUEUE)

    # Retry des messages de toutes les files MQ
    if action == "retryMessagesAllQueues":
        for SRC_QUEUE in cfg.ALL_DLQ_QUEUES:
            core.retryMessages(SRC_ENV, SRC_QUEUE)

    # Post d'un seul message
    if action == "postMessage":            
        log.info("Post du message du fichier %s vers queue %s" %(filename, DST_QUEUE))
        messagesDirectory = "messages"

        with open(os.path.join(messagesDirectory, filename)) as json_file:
            data = json.load(json_file)
            #message = "\"" + json.dumps(data).replace('"', '\\"') + "\""
            message = json.dumps(data)
            log.debug("Message %s" %(message))

            core.postMessage(SRC_ENV, DST_QUEUE, message)


if __name__ == "__main__":
    main()

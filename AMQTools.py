# -*- coding: utf-8 -*-
import sys, getopt
import src.AMQConfig as cfg
import src.AMQCore as core
import src.AMQLog as log
from tqdm import tqdm
from termcolor import colored


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho", ["help", "output"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  
        #usage()
        sys.exit(2)
    writeExcelFile = False
    for o, a in opts:
        if o in ("-h", "--help"):
            #usage()
            sys.exit()
        elif o in ("-o", "--output"):
            writeExcelFile = True
        else:
            assert False, "unhandled option"

    SRC_QUEUE = cfg.DLQ_QGENGPP
    DST_QUEUE = cfg.QGENGPP
    SRC_ENV = cfg.PRD
    DST_ENV = cfg.VAL


    log.printBanner()

    allMessages = core.getAllMessages(SRC_ENV, SRC_QUEUE)
    bodyList = core.formatMessages(allMessages, SRC_ENV, DST_QUEUE, writeExcelFile)


    if (bodyList[0] is not None):
        log.ok("post FIRST message in queue: %s %s" %(DST_QUEUE, DST_ENV))
        # postMessage(DST_ENV, DST_QUEUE, bodyList[0])

    #for message in tqdm(bodyList):
        # log.ok("OK --> post ALL messages in queue: %s %s",  %(DST_QUEUE, DST_ENV))
        #postMessage(DST_ENV, DST_QUEUE, message)


if __name__ == "__main__":
    main()

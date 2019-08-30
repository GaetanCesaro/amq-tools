# -*- coding: utf-8 -*-
import requests
import json
import difflib
import csv
import re
import sys, getopt
from openpyxl import Workbook

# Environnements
DEV = {
    "name": "DEV",
    "hostname": "http://mom-tst-01:1161",
    "broker": "ACTIVEMQ-DEV"
}

INT = {
    "name": "INT",
    "hostname": "http://mom-tst-01:2161",
    "broker": "ACTIVEMQ-INT"
}

VAL = {
    "name": "VAL",
    "hostname": "http://mom-tst-01:3161",
    "broker": "ACTIVEMQ-VAL"
}

PRD = {
    "name": "PRD",
    "hostname": "http://mom-prd-01:8161",
    "broker": "ACTIVEMQ"
}

USERNAME = "admin"
PASSWORD = "admin"

#SRC_QUEUES = ["DLQ.Consumer.SGENGPP.VirtualTopic.TDATALEGACY", "DLQ.Consumer.SGENCLI.VirtualTopic.TDATAGPP"]
#DST_QUEUES = ["Consumer.SGENGPP.VirtualTopic.TDATALEGACY", "Consumer.SGENCLI.VirtualTopic.TDATAGPP"]

SRC_QUEUE = "DLQ.Consumer.SGENGPP.VirtualTopic.TDATALEGACY"
DST_QUEUE = "Consumer.SGENGPP.VirtualTopic.TDATALEGACY"

urlGetAllMessages = "{}/api/jolokia/exec/org.apache.activemq:type=Broker,brokerName={},destinationType=Queue,destinationName={}/browse()"
#urlGetOneMessage = "{}/api/jolokia/exec/org.apache.activemq:type=Broker,brokerName={},destinationType=Queue,destinationName={}/browseMessages(java.lang.String)/JMSMessageID={}"
urlPostMessage = "{}/api/jolokia/"
bodyPostMessage = '{"type":"EXEC", "mbean":"org.apache.activemq:type=Broker,brokerName=[BROKER],destinationType=Queue,destinationName=[QUEUE]", "operation":"sendTextMessage(java.util.Map,java.lang.String,java.lang.String,java.lang.String)", "arguments":[ARGUMENTS]}'

writeExcelFile = True
excelFileName = "PRD - Messages MQ bloques.xlsx"
excelColumns = ["TABLE", "OPERATION", "dlqDeliveryFailureCause", "StringProperties", "Text"]

def getAllMessages(environnement, queue):
    response = requests.get(urlGetAllMessages.format(environnement["hostname"], environnement["broker"], queue), params=None, verify=False, auth=(USERNAME, PASSWORD))
    if (response.status_code == 200):
        jsonResponse = json.loads(response.text)
        print("getAllMessages OK")
        return jsonResponse
    else:
        print("getAllMessages ERROR")
        print(response)

def formatMessages(jsonResponse):
    messageList = []
    for message in jsonResponse["value"]:
        table = message["StringProperties"]['TABLE']
        operation = message["StringProperties"]['OPERATION']
        dlqDeliveryFailureCause = message["StringProperties"]['dlqDeliveryFailureCause']
        
        #properties = json.dumps(message["StringProperties"]).replace("u'", "'")
        properties = "{"
        headers = message["StringProperties"]
        for header in headers:
            properties = properties + "\"" + header + "\":\"" + message["StringProperties"][header] + "\", "

        properties = properties + "\"JMSDeliveryMode\":\"" + message["JMSDeliveryMode"] + "\""
        properties = properties + ", \"JMSPriority\":\"" + str(message["JMSPriority"]) + "\""
        properties = properties + "}"

        # 1ere passe de formatage
        text = json.dumps(message["Text"]).replace(' ', '').replace('\\\"', '"')
        
        argument = []
        argument.append(properties)
        argument.append(text)
        argument.append(USERNAME)
        argument.append(PASSWORD)

        if(writeExcelFile):
            ws1.append([table, operation, dlqDeliveryFailureCause, properties, text.replace('\\\"', '"').replace('"{"', '{"').replace('"}"', '"}')])
        
        # 2eme passe de formatage pour préparer le body
        argumentText = json.dumps(argument).replace('\\\"', '"').replace('\\\"', '"').replace('\\\"', '"').replace('\\\"', '"').replace('"{"', '{"').replace('"{"', '{"').replace('"}"', '"}').replace('"}"', '"}')
        messageList.append(argumentText)

    print("formatMessages OK - {} messages traites".format(len(messageList)))

    return messageList

def postMessage(environnement, queue, message):
    if(environnement["name"] == "PRD" or environnement["hostname"] == "http://mom-prd-01:8161"):
        print("postMessage ERROR - Environnement PRD interdit")
        return

    textBody = bodyPostMessage.replace("[BROKER]", environnement["broker"]).replace("[QUEUE]", queue).replace("[ARGUMENTS]", message)
    jsonBody = json.loads(textBody)

    response = requests.post(urlPostMessage.format(environnement["hostname"]), json=jsonBody, auth=(USERNAME, PASSWORD))
    if (response.status_code == 200):
        jsonResponse = json.loads(response.text)
        print("postMessage OK - HTTP Status " + str(jsonResponse["status"]))
        return jsonResponse
    else:
        print("postMessage ERROR")
        print(response)

#MAIN
wb = Workbook()
if (writeExcelFile):    
    ws1 = wb.active
    ws1.title = SRC_QUEUE[0 : 31]
    ws1.append(excelColumns)
    #ws2 = wb.create_sheet(title="TEST2")


allMessages = getAllMessages(PRD, SRC_QUEUE)
bodyList = formatMessages(allMessages)

#if (bodyList[0] is not None):
#  postMessage(VAL, DST_QUEUE, bodyList[0])

#for message in bodyList:
    #postMessage(VAL, DST_QUEUE, message)

if (writeExcelFile):
    wb.save(excelFileName)


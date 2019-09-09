# -*- coding: utf-8 -*-

# Environnements
ENVIRONNEMENTS = {
    "LOCALHOST": {
        "name": "LOCALHOST",
        "hostname": "http://localhost:8161",
        "broker": "localhost"
    },
    "DEV": {
        "name": "DEV",
        "hostname": "http://mom-tst-01:1161",
        "broker": "ACTIVEMQ-DEV1"
    },
    "INT": {
        "name": "INT",
        "hostname": "http://mom-tst-01:2161",
        "broker": "ACTIVEMQ-INT"
    },
    "VAL": {
        "name": "VAL",
        "hostname": "http://mom-tst-01:3161",
        "broker": "ACTIVEMQ-VAL"
    },
    "PRD": {
        "name": "PRD",
        "hostname": "http://mom-prd-01:8161",
        "broker": "ACTIVEMQ"
    }
}


# Login/Pswd
USERNAME = "admin"
PASSWORD = "admin"


# Messages processing
URL_GET_ALL_MESSAGES = "{}/api/jolokia/exec/org.apache.activemq:type=Broker,brokerName={},destinationType=Queue,destinationName={}/browse()"
URL_RETRY_MESSAGES = "{}/api/jolokia/exec/org.apache.activemq:type=Broker,brokerName={},destinationType=Queue,destinationName={}/retryMessages()"
#URL_GET_ONE_MESSAGE = "{}/api/jolokia/exec/org.apache.activemq:type=Broker,brokerName={},destinationType=Queue,destinationName={}/browseMessages(java.lang.String)/JMSMessageID={}"
URL_POST_MESSAGE = "{}/api/jolokia/"
BODY_POST_MESSAGE = '{"type":"EXEC", "mbean":"org.apache.activemq:type=Broker,brokerName=[BROKER],destinationType=Queue,destinationName=[QUEUE]", "operation":"sendTextMessage(java.util.Map,java.lang.String,java.lang.String,java.lang.String)", "arguments":[ARGUMENTS]}'


# Excel file configuration
OUTPUT_FOLDER = "output\\"
EXCEL_FILE_NAME = "_Messages_MQ_Bloques.xlsx"
EXCEL_COLUMNS_DLQ_Consumer_SGENGPP_VirtualTopic_TDATALEGACY = ["TABLE", "OPERATION", "dlqDeliveryFailureCause", "StringProperties", "Text"]
EXCEL_COLUMNS = ["dlqDeliveryFailureCause", "StringProperties", "Text"]

EXCEL_COLUMNS = {
    "Consumer.SGENCLI.VirtualTopic.TDATAGPP": ["dlqDeliveryFailureCause", "StringProperties", "Text"],
    "Consumer.SGENGPP.VirtualTopic.TDATALEGACY": ["TABLE", "OPERATION", "dlqDeliveryFailureCause", "StringProperties", "Text"],
    "QGENGPP": ["dlqDeliveryFailureCause", "StringProperties", "Text"],
    "QGENCLI": ["dlqDeliveryFailureCause", "StringProperties", "Text"]
}

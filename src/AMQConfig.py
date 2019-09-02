# -*- coding: utf-8 -*-

# Environnements
LOCALHOST = {
    "name": "LOCALHOST",
    "hostname": "http://localhost:8161",
    "broker": "ACTIVEMQ-LOCALHOST"
}
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

# Login/Pswd
USERNAME = "admin"
PASSWORD = "admin"

# Queues
#SRC_QUEUES = ["DLQ.Consumer.SGENGPP.VirtualTopic.TDATALEGACY", "DLQ.Consumer.SGENCLI.VirtualTopic.TDATAGPP"]
#DST_QUEUES = ["Consumer.SGENGPP.VirtualTopic.TDATALEGACY", "Consumer.SGENCLI.VirtualTopic.TDATAGPP"]
Consumer_SGENGPP_VirtualTopic_TDATALEGACY = "Consumer.SGENGPP.VirtualTopic.TDATALEGACY"
DLQ_Consumer_SGENGPP_VirtualTopic_TDATALEGACY = "DLQ.Consumer.SGENGPP.VirtualTopic.TDATALEGACY"
Consumer_SGENCLI_VirtualTopic_TDATAGPP = "Consumer.SGENCLI.VirtualTopic.TDATAGPP"
DLQ_Consumer_SGENCLI_VirtualTopic_TDATAGPP = "DLQ.Consumer.SGENCLI.VirtualTopic.TDATAGPP"
QGENGPP = "QGENGPP"
DLQ_QGENGPP = "DLQ.QGENGPP"
QGENCLI = "QGENCLI"
DLQ_QGENCLI = "DLQ.QGENCLI"



# Messages processing
URL_GET_ALL_MESSAGES = "{}/api/jolokia/exec/org.apache.activemq:type=Broker,brokerName={},destinationType=Queue,destinationName={}/browse()"
#URL_GET_ONE_MESSAGE = "{}/api/jolokia/exec/org.apache.activemq:type=Broker,brokerName={},destinationType=Queue,destinationName={}/browseMessages(java.lang.String)/JMSMessageID={}"
URL_POST_MESSAGE = "{}/api/jolokia/"
BODY_POST_MESSAGE = '{"type":"EXEC", "mbean":"org.apache.activemq:type=Broker,brokerName=[BROKER],destinationType=Queue,destinationName=[QUEUE]", "operation":"sendTextMessage(java.util.Map,java.lang.String,java.lang.String,java.lang.String)", "arguments":[ARGUMENTS]}'


# Excel file configuration
OUTPUT_FOLDER = "output\\"
EXCEL_FILE_NAME = "_Messages_MQ_Bloques.xlsx"
EXCEL_COLUMNS = ["TABLE", "OPERATION", "dlqDeliveryFailureCause", "StringProperties", "Text"]
#EXCEL_COLUMNS = ["dlqDeliveryFailureCause", "StringProperties", "Text"]

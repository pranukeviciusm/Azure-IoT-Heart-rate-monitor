import json 
import unicodedata
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from string import Template
from random import randint
import time

topic = "/Microchip/masters/2019"

##### MQTT AWS  #####

################AWS################
# For certificate based connection
myAWSIoTMQTTClient = AWSIoTMQTTClient("MastersClientID")

# For TLS mutual authentication with TLS ALPN extension
myAWSIoTMQTTClient.configureEndpoint("a3adakhi3icyv9.iot.us-west-2.amazonaws.com", 443)
myAWSIoTMQTTClient.configureCredentials("VeriSign.pem", "WSN_BE_private.pem", "WSN_BE_certificate.pem")
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myAWSIoTMQTTClient.connect()
##################################################




################### AWS Node update###############################
#Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)

##################################################
# Publish to the same topic in a loop forever
loopCount = 0
while True:
    message = {}
    message['message'] = "Hello IoT World"
    message['sequence'] = loopCount
    messageJson = json.dumps(message)
    myAWSIoTMQTTClient.publish(topic, messageJson, 1)
  
    print('Published topic %s: %s\n' % (topic, messageJson))
    loopCount += 1
    time.sleep(2)


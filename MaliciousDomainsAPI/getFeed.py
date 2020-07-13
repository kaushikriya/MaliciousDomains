from is_malicious import *


from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
# import requests
# import csv
# import time
#
#
# def getMispFeed():
#     print("reached misp feed function")
#     if (True):
#         time.sleep(2.4)
#         response= requests.get("https://panwdbl.appspot.com/lists/mdl.txt")
#         fileName="MispFolder.csv"
#         with open(fileName, 'w') as f:
#            writer = csv.writer(f)
#            for line in response.iter_lines():
#              writer.writerow(line.decode('utf-8').split(','))
#         print(" Fetching MISP malacious domain feed")
#         time.sleep(4)
#         return(True)
#
# getMispFeed()
# def IBMFeed():
#     print("response.getAuth(200)")
#     IBMFeed= requests.get("https://api.xforce.ibmcloud.com/xfti/iris/ipv4")
#     print("fetching IRIS: IPv4")
#     response={
#   "FeedCategory": "IRIS",
#   "FeedType": "IPv4",
#   "Version": "0000000010",
#   "CreationDate": "2019-08-20T07:26:00.000Z",
#   "IndicatorCount": "2",
#   "data": ["127.0.0.1", "..."]
# }
#     print('callback:' ,response)
#
# def OTXFeed():
#     print("Setting up OTX TAXII feed channel")
#     otx = OTXv2("d7ebb30c9c0854de379df59c26720fdf3d423dce810caab9edd6767871074f85")
#     pulseId= False
#     if(pulseId):
#         indicators = otx.get_pulse_indicators("pulse_id")
#         print("Pulse id required")
#         for indicator in indicators:
#            print(indicator["indicator"] + indicator["type"])
#            otx.get_indicator_details_full(IndicatorTypes.DOMAIN, "domain")
#     print("verifying OTX indicators")

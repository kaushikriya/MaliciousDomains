from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import isMalicious
import Config
import patch_pulse
import requests
import csv
import time


def getMispFeed(auth):
    status=Config.Authorisation("misp")
    if status:
        print("MISP Authorisatioon verified")
        response= requests.get("https://panwdbl.appspot.com/lists/mdl.txt")
        fileName= "MISP.csv"
        with open(fileName, 'w') as f:
           writer = csv.writer(f)
           for line in response.iter_lines():
             writer.writerow(line.decode('utf-8').split(','))
            print(" Fetched MISP malacious domain feed")
        return(True)

def IBMFeed():
    status=Config.Authorisation("IBM")
    if status:
       print("IBM Authorisation verified, status")
    IBMResponse= requests.get("https://api.xforce.ibmcloud.com/xfti/iris/ipv4")
    print("fetching IRIS: IPv4")
    fileName = "/IPv4.csv"
    with open(fileName, 'w') as f:
      writer = csv.writer(f)
      for line in IBMResponse.iter_lines():
         writer.writerow(line.decode('utf-8').split(','))
    print(" Fetched IRIS:IPv4 domain feed")
    return(True)

def OTXFeed():
    status=Config.Authorisation("OTX")
    if status:
        print("Setting up OTX TAXII feed channel")
    otx = OTXv2("d7ebb30c9c0854de379df59c26720fdf3d423dce810caab9edd6767871074f85")
    pulseId= patch_pulse.getBody()
    if(pulseId):
        indicators = otx.get_pulse_indicators("pulse_id")
        if (!indicators):
            print("Failed to fetch indicators")
        for indicator in indicators:
           print(indicator["indicator"] + indicator["type"])
           otx.get_indicator_details_full(IndicatorTypes.DOMAIN, "domain")


Run_Config=input("Configuration ")
if (Run_Config=="FETCH_UPDATE"):
    Misp=getMispFeed()
    IBM=IBMFeed()
    OTX=OTXFeed()

    if Misp && IBM && OTX:
            isMalacious.validate()

elif (Run_Config=="DOMAIN-VALIDATE"):
    isMalicious.validate()
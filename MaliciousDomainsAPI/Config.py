import requests
from setup import *

def Authorisation(id):
    if id=='misp':
        Api_key= '16e7384t73287ntx482txgf3n74f6n'
        pwd= 'fngcgh387382p217et2xgxefh847344'
        auth= requests.post("https://www.misp-project.org/feeds/",Api_key, pwd)
        return(auth)

    if id=='IBM':
        Api_key= '16e7384t73287ntx482txgf3n74f6n'
        pwd= 'fngcgh387382p217et2xgxefh847344'
        auth= requests.post("https://api.xforce.ibmcloud.com/doc/?cm_mc_uid=72618191146915921141835&cm_mc_sid_50200000=51798221594633411076&cm_mc_sid_52640000=40706841594633411095#!/Advanced_Threat_Protection_Feed/get_xfti_ew_url",Api_key, pwd)
        return(auth)

    if id=='OTX':
        Api_key= '6a32d2dc-04b2-450f-9a3f-331c971b21dc
        Pwd = '9688fcff-1ea3-49ef-9f5a-f1569ef17cbd'
        status=auth(Api_key,pwd)
        return(status)

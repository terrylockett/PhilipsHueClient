# pip install requests
# pip install keyring
import json
import keyring
import requests
import sys
import getpass
from util.configLoader import getProperty
from util.configLoader import setProperty

credsApp = 'philipsHue'
credsUser = 'phue-app'


def executeGet(url):
    resp = requests.request("GET", url, verify=False)  # TODO: disable warnings.
    if(resp.status_code != 200):
        sys.exit("Failed GET for "+url+"\n", resp.status_code, resp.text)
    return resp.text


def executePut(url, data):
    resp = requests.put(url, data, verify=False)
    if(resp.status_code != 200):
        sys.exit("Failed PUT for "+url+"\n", resp.status_code, resp.text)
    else:
        print(resp.text)


def buildUrl(endpoint):
    return getHost()+getUsername()+endpoint


def getLightsInfo():
    return json.loads(executeGet(buildUrl('/lights')))


def getGroupsInfo():
    return json.loads(executeGet(buildUrl('/groups')))


def toggleLight(id, on):
    executePut(buildUrl("/lights/"+str(id)+"/state"), data=json.dumps({"on": on}))


def toggleLightOn(id):
    lights = getLightsInfo()
    if(lights[id]['state']['on']):
        toggleLight(id, False)
    else:
        toggleLight(id, True)


def toggleGroup(id, on):
    executePut(buildUrl("/groups/"+str(id)+"/action"), data=json.dumps({"on": on}))


def toggleGroupOn(id):
    groups = getGroupsInfo()
    if(groups[id]['state']['all_on']):
        toggleGroup(id, False)
    else:
        toggleGroup(id, True)


def getUsername():
    return keyring.get_password(credsApp, credsUser)


def setUsername():
    # TODO update this to hit new user api
    print("Enter username for api")
    passwd = getpass.getpass()
    keyring.set_password(credsApp, credsUser, passwd)


def getHost():
    return getProperty('host')

def setHost(host):
    setProperty('host', host)

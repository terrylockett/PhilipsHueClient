# pip install requests
# pip install keyring
import json
import keyring
import requests
import sys
import getpass
import configparser

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


def toggleGroup(id, on):
    executePut(buildUrl("/groups/"+str(id)+"/action"), data=json.dumps({"on": on}))


def getUsername():
    return keyring.get_password(credsApp, credsUser)


def setUsername():
    # TODO update this to hit new user api
    print("Enter username for api")
    passwd = getpass.getpass()
    keyring.set_password(credsApp, credsUser, passwd)
    print("username is:", passwd)


def getHost():
    config = configparser.RawConfigParser()
    config.read('ph_config.properties')
    return config.get('Config', 'host')

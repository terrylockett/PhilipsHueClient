import sys
from util.ph_util import getLightsInfo
from util.ph_util import getGroupsInfo
from util.ph_util import toggleLight
from util.ph_util import toggleGroup
from util.ph_util import getHost
from util.ph_util import setHost
from util.ph_util import getUsername
from util.ph_util import setUsername


def handleArgs():
    print("-------------------------")
    args = sys.argv
    if(len(args) < 2):
        print("help info here... TODO")
        return

    if(args[1] == "configure"):
        handleConfigure(args)
    elif(getHost() == 'https://x.x.x.x/api/'):
        print('Hue Bridge IP is not set, run \'phue configure\' to set shit up.')


    if(args[1] == "lights"):
        handleLights(args)
    elif(args[1] == "groups"):
        handleGroups(args)

# blah


def handleConfigure(args):
    text = input("Bridge IP(leave blank to skip): ")
    if( '' != text):
        setHost(text)

    text = input("bridge api token(leave blank to skip): ")
    if( '' != text):
        setUsername(text)


def handleLights(args):
    if(len(args) <= 2):
        sys.exit("'lights' required more params..")

    lights = getLightsInfo()

    if(args[2] == "-l"):
        for id in lights.keys():
            print(id.zfill(2), ":", lights[id]["name"])

    elif(args[2] in ['-e', '-d', '-t']):
        lightId = -1
        if(args[3].isdigit()):
            lightId = int(args[3])
        else:
            sys.exit("could not find light for id", args[3])

        isEnable = True
        if(args[2] == "-d"):
            isEnable = False
        elif(args[2] == "-t"):
            isEnable = not (lights[str(lightId)]["state"]["on"])

        toggleLight(lightId, isEnable)
    else:
        sys.exit(args[2] + " is a invalid arg for 'list'")

# blh blah


def handleGroups(args):
    if(len(args) <= 2):
        sys.exit("'groups' required more params..")

    groups = getGroupsInfo()

    if(args[2] == "-l"):
        for id in groups.keys():
            print(id.zfill(2), ":", groups[id]["name"], groups[id]["lights"])

    if(args[2] in ['-e', '-d', '-t']):
        if(args[3].isdigit()):
            groupId = int(args[3])
        else:
            sys.exit("could not find group for id", args[3])

        isEnable = True
        if(args[2] == "-d"):
            isEnable = False
        elif(args[2] == "-t"):
            isEnable = not (groups[str(groupId)]["state"]["any_on"])

        toggleGroup(groupId, isEnable)


handleArgs()

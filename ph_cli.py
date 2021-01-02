import sys

from ph_util import getLightsInfo
from ph_util import getGroupsInfo
from ph_util import toggleLight
from ph_util import toggleGroup
# List lights
# List groups
# toggle light
# toggle groups
# TODO: Adjust colors


# for arg in sys.argv:
#     print(arg)
def handleArgs():
    print("-------------------------")
    args = sys.argv
    if(len(args) < 2):
        print("help info here... TODO")
        return

    if(args[1] == "lights"):
        handleLights(args)
    elif(args[1] == "groups"):
        handleGroups(args)

# blah


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

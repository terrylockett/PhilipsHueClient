import os
import yaml

configFileName = '../resources/config.yaml'


def getProperty(property):
    with open(os.path.dirname(__file__)+'/'+configFileName) as f:
        data = yaml.safe_load(f)
    return data[property]

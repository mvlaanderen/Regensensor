#!/usr/bin/env python3

__name__        = "Regensensor"
__version__     = "v1.0"
__copyright__   = "MIT"
__author__      = "Maikel Vlaanderen"
__repository__  = "https://github.com/mvlaanderen/regensensor"

import json
import requests

lat = "52.10091"
lon = "5.64627"

dataRequest = requests.get(f'https://gpsgadget.buienradar.nl/data/raintext?lat={lat}&lon={lon}').text
dataRequest = dataRequest.replace('\r\n', ' ')
dataSet = dataRequest.split()
fivemin = int(dataSet[1].split("|")[0])
tenmin = int(dataSet[2].split("|")[0])

if any([fivemin > 000, tenmin > 000]):
    print("true")
else:
    print("false")

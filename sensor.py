# sensor.py
import requests
import logging
import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME, CONF_LATITUDE, CONF_LONGITUDE
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "Regensensor"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_LATITUDE): cv.string,
    vol.Required(CONF_LONGITUDE): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    lat = config[CONF_LATITUDE]
    lon = config[CONF_LONGITUDE]

    add_entities([RegenSensor(name, lat, lon)], True)

class RegenSensor(Entity):
    def __init__(self, name, lat, lon):
        self._name = name
        self._state = None
        self._lat = lat
        self._lon = lon

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        try:
            dataRequest = requests.get(f'https://gpsgadget.buienradar.nl/data/raintext?lat={self._lat}&lon={self._lon}').text
            dataRequest = dataRequest.replace('\r\n', ' ')
            dataSet = dataRequest.split()
            fivemin = int(dataSet[1].split("|")[0])
            tenmin = int(dataSet[2].split("|")[0])

            self._state = "true" if any([fivemin > 000, tenmin > 000]) else "false"
        except Exception as e:
            _LOGGER.error(f"Error retrieving data: {e}")
            self._state = "error"

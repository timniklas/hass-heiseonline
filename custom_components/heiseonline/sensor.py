import logging

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import HeiseCoordinator

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Set up the Sensors."""
    # This gets the data update coordinator from hass.data as specified in your __init__.py
    coordinator: HeiseCoordinator = hass.data[DOMAIN][
        config_entry.entry_id
    ].coordinator

    # Enumerate all the sensors in your data value from your DataUpdateCoordinator and add an instance of your sensor class
    # to a list for each one.
    # This maybe different in your specific case, depending on how your data is structured
    sensors = []

    for index in range(1, 6):
        sensors.append(
        NewsSensor(coordinator, config_entry.title, index)
        )

    # Create the sensors.
    async_add_entities(sensors)

class NewsSensor(CoordinatorEntity):
    
    _attr_should_poll = False
    _attr_has_entity_name = True
    _attr_icon = "mdi:newspaper"
    
    def __init__(self, coordinator: HeiseCoordinator, title: str, index: int) -> None:
        super().__init__(coordinator)
        self._newsid = index
        self.name = f"Heise - {title} {index}"
        self.unique_id = f"-{title}-{index}"

    @property
    def _newsitem(self):
        return self.coordinator.data.newsitems[self._newsid - 1]

    @callback
    def _handle_coordinator_update(self) -> None:
        self.async_write_ha_state()
    
    @property
    def state(self):
        return self._newsitem['title']

    @property
    def extra_state_attributes(self):
        return {
            "summary": self._newsitem['summary'],
            "updated": self._newsitem['updated'],
            "link": self._newsitem['link']
        }

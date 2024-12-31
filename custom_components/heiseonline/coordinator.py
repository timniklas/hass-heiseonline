from dataclasses import dataclass
from datetime import timedelta
import logging
import feedparser
import re

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_LOCATION,
    CONF_NAME,
    CONF_SELECTOR
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from aiohttp import ClientError
from xml.dom import minidom

from homeassistant.const import (
    CONF_URL
)

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


@dataclass
class HeiseAPIData:
    """Class to hold api data."""

    newsitems: [any]


class HeiseCoordinator(DataUpdateCoordinator):
    """My coordinator."""

    data: HeiseAPIData

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:
        """Initialize coordinator."""

        # Set variables from values entered in config flow setup
        self._url = config_entry.data[CONF_URL]

        # Initialise DataUpdateCoordinator
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN} ({config_entry.unique_id})",
            # Method to call on every update interval.
            update_method=self.async_update_data,
            # Polling interval. Will only be polled if there are subscribers.
            update_interval=timedelta(seconds=60),
        )
        self.connected: bool = False
        self._hass = hass

    async def async_update_data(self):
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        try:
            feed = await self._hass.async_add_executor_job(feedparser.parse, self._url)
            items = []
            for element in feed.entries:
                items.append({
                    "title": element['title'],
                    "summary": element['summary'],
                    "updated": element['updated'],
                    "link": element['link']
                })
            self.connected = True
            return HeiseAPIData(newsitems=items)
                
        except ClientError as err:
            # This will show entities as unavailable by raising UpdateFailed exception
            raise UpdateFailed(f"Error communicating with API: {err}") from err

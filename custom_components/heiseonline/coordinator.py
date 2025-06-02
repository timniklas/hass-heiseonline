from dataclasses import dataclass
from datetime import timedelta
import logging
import atoma
from bs4 import BeautifulSoup
import aiohttp

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from aiohttp import ClientError

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
        self.websession = async_get_clientsession(hass)

    async def async_update_data(self):
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        try:
            async with self.websession.get(self._url) as response:
                response.raise_for_status()
                response_bytes = await response.read()
                cleaned = BeautifulSoup(response_bytes, "xml").prettify()
                feed = atoma.parse_atom_bytes(cleaned.encode("utf-8"))
                
                items = []
                for entry in feed.entries:
                    if entry.title is None:
                        continue
                    if entry.summary is None:
                        continue
                    if entry.updated is None:
                        continue
                    if len(entry.links) < 1:
                        continue

                    items.append({
                        "title": entry.title.value,
                        "summary": entry.summary.value,
                        "updated": entry.updated,
                        "link": entry.links[0].href
                    })
                self.connected = True
                return HeiseAPIData(newsitems=items)
        except ClientError as err:
            # This will show entities as unavailable by raising UpdateFailed exception
            raise UpdateFailed(f"Error communicating with API: {err}") from err

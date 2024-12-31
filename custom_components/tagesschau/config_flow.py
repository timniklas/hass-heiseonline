import voluptuous as vol
from homeassistant.config_entries import ConfigFlow
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from aiohttp import ClientError, ClientResponseError, ClientSession

from homeassistant.const import (
    CONF_URL
)

from .const import (
    DOMAIN,
    FEEDS
)

class HeiseConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 2

    def __init__(self) -> None:
        """Initialize the config flow."""

    async def async_step_user(self, formdata):
        if formdata is not None:
            feed_url = formdata[CONF_URL]
            feed_name = FEEDS[feed_url]
            return self.async_create_entry(title=f"{feed_name}",data=formdata)

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(
                {vol.Required(CONF_URL): vol.In(FEEDS)}
            ),
        )

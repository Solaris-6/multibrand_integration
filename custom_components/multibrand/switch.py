"""Switch platform for Multibrand integration."""
import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity, SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the switch platform."""
    multibrand_data = hass.data.get(DOMAIN, {})
    devices = multibrand_data.get("devices", {})
    all_products = multibrand_data.get("all_products", {})
    
    entities = []

    for brand, info in devices.items():
        # Get all products for this brand
        brand_products = []
        for product_id, product_data in all_products.items():
            if product_id.startswith(brand + "_"):
                product_data_copy = product_data.copy()
                product_data_copy['brand'] = brand
                brand_products.append(product_data_copy)
        
        for product in brand_products:
            # Only create switches for switch-type products
            if product.get("type") in ["smart_switch", "smart_plug", "smart_thermostat"]:
                entities.append(MultibrandSwitch(product))

    async_add_entities(entities, True)


class MultibrandSwitch(SwitchEntity):
    """Representation of a multibrand switch."""

    def __init__(self, product: dict[str, Any]):
        """Initialize the switch."""
        self._product = product
        self._attr_name = f"{product['name']} switch"
        self._attr_unique_id = f"{product['id']}_switch"
        self._attr_has_entity_name = True
        self._is_on = False

    @property
    def name(self) -> str:
        """Return the name of the switch."""
        return self._attr_name

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return self._attr_unique_id

    @property
    def is_on(self) -> bool:
        """Return true if switch is on."""
        return self._is_on

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        self._is_on = True
        self.async_write_ha_state()
        _LOGGER.info("Turning on %s", self._product.get("name"))

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        self._is_on = False
        self.async_write_ha_state()
        _LOGGER.info("Turning off %s", self._product.get("name"))

"""Device tracker platform for Multibrand integration."""
import logging
from typing import Any

from homeassistant.components.device_tracker import DeviceTrackerEntity, DeviceTrackerEntityDescription
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
    """Set up the device tracker platform."""
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
            # Only create device trackers for sensor-type products
            if product.get("type") in ["smart_sensor", "temperature_humidity", "smart_thermostat"]:
                entities.append(MultibrandDeviceTracker(product))

    async_add_entities(entities, True)


class MultibrandDeviceTracker(DeviceTrackerEntity):
    """Representation of a multibrand device tracker."""

    def __init__(self, product: dict[str, Any]):
        """Initialize the device tracker."""
        self._product = product
        self._attr_name = f"{product['name']} tracker"
        self._attr_unique_id = f"{product['id']}_tracker"
        self._attr_has_entity_name = True
        self._attr_available = False

    @property
    def name(self) -> str:
        """Return the name of the device tracker."""
        return self._attr_name

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return self._attr_unique_id

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self._available

    @property
    def device_state_attributes(self) -> dict[str, Any]:
        """Return device state attributes."""
        return {
            "brand": self._product.get("brand"),
            "product_type": self._product.get("type"),
            "product_id": self._product.get("name"),
            "config": self._product,
        }

    async def async_update(self) -> None:
        """Update device tracker state."""
        # Probe device availability based on product type
        product_type = self._product.get("type")
        if product_type in ["smart_sensor", "temperature_humidity", "smart_thermostat"]:
            self._available = True

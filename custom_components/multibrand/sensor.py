"""Sensor platform for Multibrand integration."""
import logging
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the sensor platform."""
    multibrand_data = hass.data.get("multibrand", {})
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
            entities.append(MultibrandSensor(brand, product))
    
    async_add_entities(entities, True)


class MultibrandSensor(Entity):
    """Representation of a multibrand sensor."""

    def __init__(self, brand, product):
        """Initialize the sensor."""
        self._brand = brand
        self._product = product
        self._attr_name = f"{product['name']} sensor"
        self._attr_unique_id = f"{brand}_{product['name'].lower().replace(' ', '_')}_sensor"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._attr_name

    @property
    def unique_id(self):
        """Return a unique ID."""
        return self._attr_unique_id

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._product.get("power", "unknown")

    @property
    def extra_state_attributes(self):
        """Return state attributes."""
        return {
            "brand": self._brand,
            "product_type": self._product.get("type"),
            "product_id": self._product.get("name"),
            "config": self._product
        }

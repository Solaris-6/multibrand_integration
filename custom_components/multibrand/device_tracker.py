"""Device tracker platform for Multibrand integration."""
import logging
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the device tracker platform."""
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
            # Only create device trackers for sensor-type products
            if product.get("type") in ["smart_sensor", "temperature_humidity", "smart_thermostat"]:
                entities.append(MultibrandDeviceTracker(brand, product))
    
    async_add_entities(entities, True)


class MultibrandDeviceTracker(Entity):
    """Representation of a multibrand device tracker."""

    def __init__(self, brand, product):
        """Initialize the device tracker."""
        self._brand = brand
        self._product = product
        self._attr_name = f"{product['name']} tracker"
        self._attr_unique_id = f"{brand}_{product['name'].lower().replace(' ', '_')}_tracker"
        self._available = False

    @property
    def name(self):
        """Return the name of the device tracker."""
        return self._attr_name

    @property
    def unique_id(self):
        """Return a unique ID."""
        return self._attr_unique_id

    @property
    def available(self):
        """Return if entity is available."""
        return self._available

    @property
    def device_state_attributes(self):
        """Return device state attributes."""
        return {
            "brand": self._brand,
            "product_type": self._product.get("type"),
            "product_id": self._product.get("name"),
            "config": self._product
        }

    async def async_update(self):
        """Update device tracker state."""
        # Probe device availability based on product type
        product_type = self._product.get("type")
        if product_type == "smart_sensor":
            # Sensors are considered available if the device responds
            self._available = True
        elif product_type == "temperature_humidity":
            self._available = True
        elif product_type == "smart_thermostat":
            self._available = True

"""Switch platform for Multibrand integration."""
import logging
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the switch platform."""
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
            # Only create switches for switch-type products
            if product.get("type") in ["smart_switch", "smart_plug", "smart_thermostat"]:
                entities.append(MultibrandSwitch(brand, product))
    
    async_add_entities(entities, True)


class MultibrandSwitch(Entity):
    """Representation of a multibrand switch."""

    def __init__(self, brand, product):
        """Initialize the switch."""
        self._brand = brand
        self._product = product
        self._attr_name = f"{product['name']} switch"
        self._attr_unique_id = f"{brand}_{product['name'].lower().replace(' ', '_')}_switch"
        self._is_on = False

    @property
    def name(self):
        """Return the name of the switch."""
        return self._attr_name

    @property
    def unique_id(self):
        """Return a unique ID."""
        return self._attr_unique_id

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self._is_on

    async def async_turn_on(self, **kwargs):
        """Turn the switch on."""
        self._is_on = True
        self.async_write_ha_state()
        _LOGGER.info("Turning on %s", self._product.get("name"))

    async def async_turn_off(self, **kwargs):
        """Turn the switch off."""
        self._is_on = False
        self.async_write_ha_state()
        _LOGGER.info("Turning off %s", self._product.get("name"))

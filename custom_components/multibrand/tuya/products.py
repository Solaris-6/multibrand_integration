# Tuya smart product catalog - Unified export
TUYA_PRODUCTS = {
    'tuya_switch': {'name': 'Tuya Switch', 'type': 'smart_switch', 'port': 80, 'api': '/sm', 'power': True},
    'tuya_plug': {'name': 'Tuya Plug', 'type': 'smart_plug', 'port': 80, 'api': '/sm', 'power': True},
    'tuya_dimmer': {'name': 'Tuya Dimmer', 'type': 'smart_switch', 'port': 80, 'api': '/sm', 'channels': 1},
    'tuya_sensor': {'name': 'Tuya Sensor', 'type': 'smart_sensor', 'port': 80, 'api': '/data', 'motion': True, 'temperature': True},
    'tuya_humidity': {'name': 'Tuya Humidity', 'type': 'temperature_humidity', 'port': 80, 'api': '/data', 'temp': True, 'humidity': True},
    'tuya_light': {'name': 'Tuya Light', 'type': 'smart_light', 'port': 80, 'api': '/sm', 'color': True},
    'tuya_gateway': {'name': 'Tuya Gateway', 'type': 'smart_switch', 'port': 80, 'api': '/sm', 'power': True},
}

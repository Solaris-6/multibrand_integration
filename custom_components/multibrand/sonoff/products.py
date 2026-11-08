# Sonoff smart product catalog - Unified export
SONOFF_PRODUCTS = {
    'sonoff_basic': {'name': 'Sonoff Basic', 'type': 'smart_switch', 'port': 8080, 'api': '/', 'power': True},
    'sonoff_basic_r4': {'name': 'Sonoff Basic R4', 'type': 'smart_switch', 'port': 8080, 'api': '/e/proc/set', 'power': True},
    'sonoff_mini': {'name': 'Sonoff Mini', 'type': 'smart_switch', 'port': 8080, 'api': '/e/proc/set', 'power': True},
    'sonoff_power': {'name': 'Sonoff POW', 'type': 'energy_monitor', 'port': 8080, 'api': '/get', 'power': True, 'energy': True},
    'sonoff_th': {'name': 'Sonoff TH', 'type': 'temperature_humidity', 'port': 8080, 'api': '/e/voice', 'temp': True, 'humidity': True},
    'sonoff_pm': {'name': 'Sonoff PM', 'type': 'power_meter', 'port': 8080, 'api': '/get', 'power': True},
    'sonoff_snzb': {'name': 'Sonoff Zigbee', 'type': 'smart_sensor', 'port': 8080, 'api': '/e/voice', 'motion': True, 'temperature': True, 'humidity': True},
    'sonoff_s26rf': {'name': 'Sonoff S26RF', 'type': 'smart_switch', 'port': 8080, 'api': '/e/proc/set', 'power': True},
    'sonoff_r4': {'name': 'Sonoff R4', 'type': 'smart_sensor', 'port': 8080, 'api': '/get', 'motion': True, 'temperature': True, 'humidity': True},
}

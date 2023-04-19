import json
import psutil
import paho.mqtt.client as mqtt
import time
import os

# Set the MQTT topic prefix and device name
TOPIC_PREFIX = "homeassistant/sensor"
DEVICE_NAME = "laptop"

# Create the MQTT client
client = mqtt.Client()

# Set the MQTT broker credentials
client.username_pw_set(
    username=os.environ.get("MQTT_BROKER_USERNAME"),
    password=os.environ.get("MQTT_BROKER_PASSWORD")
)

# Connect to the MQTT broker
client.connect(
    host=os.environ.get("MQTT_BROKER_HOST"),
    port=1883,
    keepalive=60
)

# Start the MQTT client loop
client.loop_start()

# Continuously publish the laptop info
while True:
    # Get the info

    battery = psutil.sensors_battery()
    battery_percentage = battery.percent
    battery_round = round(battery_percentage)
    battery_plugged = battery.power_plugged
    disk_usage = psutil.disk_usage("/")
    total_storage = round(disk_usage.total / (1024**3), 2)
    free_storage = round(disk_usage.free / (1024**3), 2)
    used_storage = round(disk_usage.used / (1024**3), 2)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    cpu_percent = psutil.cpu_percent()

    payload = json.dumps({
        "state": battery_percentage,
        "unit_of_measurement": "%"
    })
    client.publish(
        f"{TOPIC_PREFIX}/{DEVICE_NAME}_battery/state",
        payload=battery_round,
        retain=True
    )
    payload = json.dumps({
        "state": battery_plugged,
    })
    client.publish(
        f"{TOPIC_PREFIX}/{DEVICE_NAME}_battery_status/state",
        payload=battery_plugged,
        retain=True
    )
    payload = json.dumps({
        "state": cpu_percent,
        "unit_of_measurement": "%"
    })
    client.publish(
        f"{TOPIC_PREFIX}/{DEVICE_NAME}_cpu_percent/state",
        payload=cpu_percent,
        retain=True
    )
    payload = json.dumps({
        "state": used_storage,
    })
    client.publish(
        f"{TOPIC_PREFIX}/{DEVICE_NAME}_storage_used/state",
        payload=used_storage,
        retain=True
    )
    payload = json.dumps({
        "state": total_storage,
    })
    client.publish(
        f"{TOPIC_PREFIX}/{DEVICE_NAME}_storage_total/state",
        payload=total_storage,
        retain=True
    )
    payload = json.dumps({
        "state": free_storage,
    })
    client.publish(
        f"{TOPIC_PREFIX}/{DEVICE_NAME}_storage_free/state",
        payload=free_storage,
        retain=True
    )
    # Wait for the next interval
    time.sleep(int(os.environ.get("MQTT_DISCOVERY_INTERVAL")))

# linuxlaptopstat2mqtt
it is a docker container for sending linux computer stats to mqtt broker
```bash
  docker run -d \
  --name=linuxlaptopstat2mqtt \
  -e MQTT_BROKER_HOST=yourmqtthost \
  -e MQTT_BROKER_PORT=1883 \
  -e MQTT_BROKER_USERNAME=yourmqttusername \
  -e MQTT_BROKER_PASSWORD=yourmqttpassword \
  --restart unless-stopped \
   indiantechie/linuxlaptopstats2mqtt:latest

```
then add the following to your mqtt.yaml
```bash
sensor:
  - name: "Battery Percentage"
    state_topic: "homeassistant/sensor/laptop_battery/state"
    unique_id: "laptop_battery"
    icon: mdi:battery
    unit_of_measurement: "%"
    device:
      identifiers:
        - laptop
      manufacturer: "HP"
      model: "Pavillion-X360"
      name: "Jash Laptop"
  - name: "Battery Plugged"
    state_topic: "homeassistant/sensor/laptop_battery_status/state"
    unique_id: "laptop_battery_plugged"
    icon: mdi:battery-sync-outline
    device:
      identifiers:
        - laptop
      manufacturer: "HP"
      model: "Pavillion-X360"
      name: "Jash Laptop"
  - name: "CPU Percentage"
    state_topic: "homeassistant/sensor/laptop_cpu_percent/state"
    unique_id: "laptop_cpu_percent"
    icon: mdi:cpu-64-bit
    unit_of_measurement: "%"
    device:
      identifiers:
        - laptop
      manufacturer: "HP"
      model: "Pavillion-X360"
      name: "Jash Laptop"
  - name: "Total Storage"
    state_topic: "homeassistant/sensor/laptop_storage_total/state"
    unique_id: "laptop_storage_total"
    icon: mdi:harddisk
    unit_of_measurement: Gb
    device:
      identifiers:
        - laptop
      manufacturer: "HP"
      model: "Pavillion-X360"
      name: "Jash Laptop"
  - name: "Used Storage"
    state_topic: "homeassistant/sensor/laptop_storage_used/state"
    unique_id: "laptop_storage_used"
    icon: mdi:harddisk-remove
    unit_of_measurement: Gb
    device:
      identifiers:
        - laptop
      manufacturer: "HP"
      model: "Pavillion-X360"
      name: "Jash Laptop"
  - name: "Free Storage"
    state_topic: "homeassistant/sensor/laptop_storage_free/state"
    unique_id: "laptop_storage_free"
    icon: mdi:harddisk-plus
    unit_of_measurement: Gb
    device:
      identifiers:
        - laptop
      manufacturer: "HP"
      model: "Pavillion-X360"
      name: "Jash Laptop"



```

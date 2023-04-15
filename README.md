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
  - name: "Laptop Battery"
    state_topic: "homeassistant/sensor/laptop_battery/state"
    unique_id: "laptop_battery"
    icon: mdi:battery
    device:
      identifiers:
        - laptop
      manufacturer: "yourmanufacturer"
      model: "your model"
      name: "your laptop name"


```

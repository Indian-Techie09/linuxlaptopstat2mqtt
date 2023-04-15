# linuxlaptopstat2mqtt
it is a docker container for sending linux computer stats to mqtt broker
```bash
  docker run -d \
  --name=linuxlaptopstat2mqtt \
  -e MQTT_BROKER_HOST=9.9.8.101 \
  -e MQTT_BROKER_PORT=1883 \
  -e MQTT_BROKER_USERNAME=mqtt \
  -e MQTT_BROKER_PASSWORD=mqtt2724 \
  --restart unless-stopped \
   indiantechie/linuxlaptopstats2mqtt:latest

```

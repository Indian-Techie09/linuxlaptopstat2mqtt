FROM python:3.8-slim-buster

# Install necessary packages
RUN apt-get update && \
    apt-get install -y mosquitto-clients

# Create a directory for the application
WORKDIR /app

# Copy the necessary files
COPY requirements.txt .
COPY linuxlaptopstats2mqtt.py .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variables
ENV MQTT_BROKER_HOST=your-mqtt-broker-host
ENV MQTT_BROKER_PORT=your-mqtt-broker-port
ENV MQTT_BROKER_USERNAME=your-mqtt-broker-username
ENV MQTT_BROKER_PASSWORD=your-mqtt-broker-password
ENV MQTT_DISCOVERY_INTERVAL=10

# Run the application
CMD ["python", "linuxlaptopstats2mqtt.py"]

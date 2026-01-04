import paho.mqtt.client as mqtt
import json
import time
import random

# Cấu hình MQTT
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
DEVICE_ID = "zigbee_temp_sensor_01"
DISCOVERY_PREFIX = "homeassistant"

# Tạo MQTT client
client = mqtt.Client()

def publish_discovery():
    """Gửi MQTT Discovery để HA tự động nhận diện thiết bị"""
    
    # Discovery cho sensor nhiệt độ
    temp_config = {
        "name": "Living Room Temperature",
        "device_class": "temperature",
        "state_topic": f"zigbee/{DEVICE_ID}/state",
        "unit_of_measurement": "°C",
        "value_template": "{{ value_json.temperature }}",
        "unique_id": f"{DEVICE_ID}_temp",
        "device": {
            "identifiers": [DEVICE_ID],
            "name": "Zigbee Temperature Sensor",
            "model": "DHT22",
            "manufacturer": "Simulated Device"
        }
    }
    
    # Discovery cho sensor độ ẩm
    humidity_config = {
        "name": "Living Room Humidity",
        "device_class": "humidity",
        "state_topic": f"zigbee/{DEVICE_ID}/state",
        "unit_of_measurement": "%",
        "value_template": "{{ value_json.humidity }}",
        "unique_id": f"{DEVICE_ID}_humidity",
        "device": {
            "identifiers": [DEVICE_ID],
            "name": "Zigbee Temperature Sensor",
            "model": "DHT22",
            "manufacturer": "Simulated Device"
        }
    }
    
    # Publish discovery messages
    client.publish(
        f"{DISCOVERY_PREFIX}/sensor/{DEVICE_ID}_temp/config",
        json.dumps(temp_config),
        retain=True
    )
    
    client.publish(
        f"{DISCOVERY_PREFIX}/sensor/{DEVICE_ID}_humidity/config",
        json.dumps(humidity_config),
        retain=True
    )
    
    print("✓ Discovery messages published")

def publish_sensor_data():
    """Gửi dữ liệu cảm biến"""
    temperature = round(random.uniform(20.0, 30.0), 1)
    humidity = round(random.uniform(40.0, 70.0), 1)
    
    payload = {
        "temperature": temperature,
        "humidity": humidity,
        "battery": random.randint(80, 100)
    }
    
    client.publish(
        f"zigbee/{DEVICE_ID}/state",
        json.dumps(payload)
    )
    
    print(f"Published: Temp={temperature}°C, Humidity={humidity}%")

# Kết nối và chạy
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✓ Connected to MQTT Broker")
        publish_discovery()
    else:
        print(f"✗ Connection failed with code {rc}")

client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

# Gửi dữ liệu mỗi 5 giây
try:
    while True:
        publish_sensor_data()
        time.sleep(5)
except KeyboardInterrupt:
    print("\n✓ Script stopped")
    client.loop_stop()
    client.disconnect()

import paho.mqtt.client as mqtt
import json
import time
import threading
import random

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
NUM_DEVICES = 50  # Số lượng thiết bị giả lập
MESSAGES_PER_SECOND = 10

def simulate_device(device_id):
    """Mô phỏng một thiết bị"""
    client = mqtt.Client(
    	client_id=f"stress_test_{device_id}",
    	callback_api_version=mqtt.CallbackAPIVersion.VERSION1
    )
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    
    while True:
        for _ in range(MESSAGES_PER_SECOND):
            payload = {
                "temperature": round(random.uniform(15.0, 35.0), 1),
                "humidity": round(random.uniform(30.0, 80.0), 1)
            }
            
            client.publish(
                f"stress_test/device_{device_id}/state",
                json.dumps(payload)
            )
            
            time.sleep(1 / MESSAGES_PER_SECOND)

# Khởi động nhiều threads
print(f"Starting stress test with {NUM_DEVICES} devices...")
threads = []

for i in range(NUM_DEVICES):
    thread = threading.Thread(target=simulate_device, args=(i,))
    thread.daemon = True
    thread.start()
    threads.append(thread)

print("Stress test running. Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping stress test...")

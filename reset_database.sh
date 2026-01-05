#!/bin/bash

echo ">>> STOPPING CONTAINERS"
docker compose down

echo ">>> RESETTING MARIADB DATA"
sudo rm -rf mariadb/*

echo ">>> STARTING SYSTEM"
docker compose up -d

echo ">>> WAITING FOR MARIADB..."
sleep 10

echo ">>> VERIFY DATABASE STATE"
docker exec -it mariadb mariadb S -u homeassistant -phomeassistant_pass homeassistant <<EOF
SELECT COUNT(*) AS states_count FROM states;
SELECT COUNT(*) AS events_count FROM events;
EOF

echo ">>> RESET DONE"

#!/usr/bin/with-contenv bashio

echo "Starting Hermes ...."

export HASS_URL=$(bashio::config 'hass_url')
export HASS_TOKEN=$(bashio::config 'hass_token')

exec python3 /server.py
#!/usr/bin/with-contenv bashio

echo "Starting Hermes Bridge..."

export HASS_URL=$(bashio::config 'hass_url')
export HASS_TOKEN=$(bashio::config 'hass_token')

exec python /server.py
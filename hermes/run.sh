#!/usr/bin/with-contenv bashio

export HASS_URL=$(bashio::config 'hass_url')
export HASS_TOKEN=$(bashio::config 'hass_token')

python /server.py
#!/usr/bin/with-contenv bashio

export HASS_URL=$(bashio::config 'hass_url')
export HASS_TOKEN=$(bashio::config 'hass_token')

uvicorn server:app --host 0.0.0.0 --port 8080
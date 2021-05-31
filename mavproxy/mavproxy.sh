#!/bin/sh
echo "${AIRCRAFT_NAME}"
echo "${VEHICLE_TYPE}"
echo "${VEHICLE_ADDR}"
echo "${APP_ADDR}"

mavproxy.py --aircraft="${AIRCRAFT_NAME}"  --"${VEHICLE_TYPE}" --master="${VEHICLE_ADDR}" --out "${APP_ADDR}"
#!/usr/bin/env bash

address=`cat lockaddr`
res=$(curl $address -X GET)
if [[ $res == *"true"* ]]; then
    curl $address -X PUT -H "Content-Type: application/json" -d "{\"status\":false}"
else
    curl $address -X PUT -H "Content-Type: application/json" -d "{\"status\":true}"
fi

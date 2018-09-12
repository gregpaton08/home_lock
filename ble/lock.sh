#!/usr/bin/env bash

address=`cat lockaddr`
curl $address -X PUT -H "Content-Type: application/json" -d "{\"status\":true}"

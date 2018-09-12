#!/usr/bin/env bash

address=`cat lockaddr`
res=$(curl $address -X GET > /dev/null 2>&1)
if [[ $res == *"true"* ]]; then
    echo 1
else
    echo 0
fi

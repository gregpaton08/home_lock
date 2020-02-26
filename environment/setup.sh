#!/usr/bin/env bash

# get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${DIR}/..

venv_dir="venv"
if [ ! -d "$venv_dir" ]; then
    python3 -m venv venv
    venv/bin/pip install -r ${DIR}/requirements.txt
fi

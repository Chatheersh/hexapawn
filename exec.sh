#!/bin/bash
DIR="$(realpath $( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd ))"

PYTHONPATH=$DIR:$PYTHONPATH \
    poetry run python3 $DIR/hexapawn/main.py

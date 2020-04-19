#!/bin/bash

export FLASK_APP=receive_image.py
export FLASK_DEBUG=0

flask run --host 0.0.0.0 &

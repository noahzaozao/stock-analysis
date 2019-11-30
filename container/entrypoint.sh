#!/bin/sh

cd /usr/src/app &&
gunicorn -b :8000 app:app

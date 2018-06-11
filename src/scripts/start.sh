#!/bin/bash

uwsgi --http :8000 --file /home/scout/stem/src/python/app.py --callable app --py-autoreload 1
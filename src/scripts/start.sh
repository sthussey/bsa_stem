#!/bin/bash
uwsgi --http :8000 --file /home/scout/stem/src/python/stem/app.py --callable app --py-autoreload 1 --pp /home/scout/stem/src/python

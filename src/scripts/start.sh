#!/bin/bash
uwsgi --http :8000 \
      --file /home/scout/stem/python/stem/app.py \
      --callable app \
      --py-autoreload 1 \
      --pp /home/scout/stem/python \
      --check-static /home/scout/stem/web \
      --logger file:/var/log/uwsgi.log

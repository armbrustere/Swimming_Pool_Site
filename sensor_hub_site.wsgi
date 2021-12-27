#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/sensor_hub_site/")

from sensor_hub_site import app as application

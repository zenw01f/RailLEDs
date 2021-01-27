#!/usr/bin/env python3
# Das Blinkenlights Scheduler Daemon

import sys
sys.path.append('/opt/blinkenlights/das_blinkenlights/APA102_Pi')
import os
import re
import random
import argparse
import threading
import calendar
import datetime
from datetime import date, datetime, time
from colorcycletemplate import ColorCycleTemplate
import colorschemes

NUM_LED = 646
BASE_PATH = '/opt/blinkenlights/das_blinkenlights'
SCHEDULE_PATH = BASE_PATH + '/schedule.d'

"""
Read schedule files, similar to crontab format


# Schedule file format:
# 0 = Sunday
# min hr dom mon dow	sequence
  0   18 *   *   1-5	slow_rainbow
  0   15 *   *   6	slow_rainbow
  0   22 *   *   1-6	lights_off


Program flow:

init:
- Read in schedule
- Start listener

loop:
- 



"""


for filename in os.listdir(SCHEDULE_PATH):
  file = open(SCHEDULE_PATH + "/" + filename, "r")
  for line in file:
    print(line)

  file.close()


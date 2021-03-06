#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import sys
sys.path.append('/opt/blinkenlights/das_blinkenlights/APA102_Pi')

import datetime
import calendar
from datetime import date, datetime, time
import argparse
from colorcycletemplate import ColorCycleTemplate
import colorschemes

NUM_LED = 646

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('num_led', type=int, default=646, nargs='?',
                        help='The number of LEDs in the strip')
    parser.add_argument('mosi', type=int, default=10, nargs='?',
                        help='The pin for SPI MOSI. 10 corresponds to the Raspberry Pi hardware SPI.'
                        ' Set negative for console debug.')
    parser.add_argument('sclk', type=int, default=11, nargs='?',
                        help='The pin for SPI SCLK. 11 corresponds to the Raspberry Pi hardware SPI.')
    parser.add_argument('--patterns', type=int, default=range(100), nargs='+',
                        help='Controls which test patterns run.')
    args = parser.parse_args()

    options = {
        'num_led': args.num_led,
        'mosi': args.mosi,
        'sclk': args.sclk,
    }

    def in_between(now, start, end):
      if start <= end:
        return start <= now < end
      else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end

    try:
      while True:
        MY_CYCLE = colorschemes.Chaser(num_steps_per_cycle=options['num_led'], pause_value=0.02, num_cycles=10,
                                              **options)
        MY_CYCLE.start()

    except KeyboardInterrupt:
      pass

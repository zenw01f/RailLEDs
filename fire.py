#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import sys
sys.path.append('/opt/blinkenlights/das_blinkenlights/APA102_Pi')

from apa102 import Pixel
import argparse
from colorcycletemplate import ColorCycleTemplate
import colorschemes

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display a larson scanner.')
    parser.add_argument('num_led', type=int, default=646, nargs='?',
                        help='The number of LEDs in the strip')
    parser.add_argument('mosi', type=int, default=10, nargs='?',
                        help='The pin for SPI MOSI. 10 corresponds to the Raspberry Pi hardware SPI.'
                        ' Set negative for console debug.')
    parser.add_argument('sclk', type=int, default=11, nargs='?',
                        help='The pin for SPI SCLK. 11 corresponds to the Raspberry Pi hardware SPI.')
    args = parser.parse_args()

    options = {
        'num_led': args.num_led,
        'mosi': args.mosi,
        'sclk': args.sclk,
    }

    MY_CYCLE = ColorCycleTemplate(pause_value=0.02, num_steps_per_cycle=60, num_cycles=20,
                                  **options)
    num_updaters = 1
    sec_width = args.num_led // num_updaters
    sec_ranges = list(zip(range(0, args.num_led, sec_width), range(sec_width-1, args.num_led, sec_width)))
    sec_ranges[-1] = (sec_ranges[-1][0], args.num_led-1) # Make sure we get them all
    MY_CYCLE.append_updater(colorschemes.create_fire(*sec_ranges.pop(0)))
    MY_CYCLE.append_updater(colorschemes.add_delay(1))
    MY_CYCLE.start()


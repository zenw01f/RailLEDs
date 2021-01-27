#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import sys
sys.path.append('/opt/blinkenlights/das_blinkenlights/APA102_Pi')

from apa102 import APA102, Pixel
import time

# Initialize the library and the strip
strip = APA102(num_led=646, global_brightness=20, mosi = 10, sclk = 11,
                      order='rbg')

# Turn off all pixels (sometimes a few light up when the strip gets power)
strip.clear_strip()


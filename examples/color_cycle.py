import os
import sys
from PIL import Image, ImageDraw
import time
import numpy as np

from st7735_tft import ST7735_TFT               # To test higher speed library
# from ST7735 import ST7735 as ST7735_TFT       # To test original Pimoroni library


disp = ST7735_TFT(
    port=0,
    cs=0,
    dc=9,
    backlight=19,
    spi_speed_hz=4000000,
    # rotation=0
)
img = Image.new('RGB', (disp.width, disp.height), '#000000')
painter = ImageDraw.Draw(img)

steps = 100

t = time.time()
for color in np.linspace(0, 360, steps):
    color = 'hsv({}, 100%, 100%)'.format(np.floor(color))
    painter.rectangle(((0,0), img.size), fill=color)
    disp.display(img)
time_per_frame = (time.time() - t) / steps
print('Average framerate for full screen update: {:.2f}'.format(1 / time_per_frame))

# Clear screen
painter.rectangle(((0,0), img.size), fill='#000000')

# Static part of image
painter.rectangle(((50, 50), (70, 70)), fill='#0000FF')
disp.display(img)

size = 50
t = time.time()
for color in np.linspace(0, 360, steps):
    color = 'hsv({}, 100%, 100%)'.format(np.floor(color))
    painter.rectangle(((0,0), (size,size)), fill=color)
    disp.display(img)
time_per_frame = (time.time() - t) / steps
print('Average framerate for partial screen update ({:.2f}) pixels): {}'.format(size**2, 1/time_per_frame))

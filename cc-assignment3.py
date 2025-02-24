import random
import os
import time
import math

os.system('cls | clear')  # Clear the screen

EMPTY = ' '
MIN_DELAY = 0.05  # Minimum delay
MAX_DELAY = .5  # Maximum delay
DELAY_INCREMENT = 0.02  # Increment for delay change
DELAY = MIN_DELAY  # Start with the minimum delay
direction = 1  # 1 for increasing, -1 for decreasing

CHARS = []
SINE_STEP_INCS = []
sine_steps = []
for i in range(random.randint(7, 25)):
    CHARS.append(random.choice('aisha,ツ,`*:;,．★'))
    SINE_STEP_INCS.append(random.random() * 0.1 + 0.0001)
    sine_steps.append(random.random() * math.pi)

WIDTH = 120  # Width of the terminal

try:
    while True:
        row = [EMPTY] * WIDTH

        for i in range(len(CHARS)):
            row[int((math.sin(sine_steps[i]) + 1) / 2 * WIDTH)] = CHARS[i]
            sine_steps[i] += SINE_STEP_INCS[i]

        print(''.join(row))

        time.sleep(DELAY)

        # Update the delay
        DELAY += DELAY_INCREMENT * direction

        # Reverse direction if we hit the min or max delay
        if DELAY >= MAX_DELAY or DELAY <= MIN_DELAY:
            direction *= -1

except KeyboardInterrupt:
    print('Helix Travels, by Al Sweigart al@inventwithpython.com 2024')

    #python3 cc-assignment3.py
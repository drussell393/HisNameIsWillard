#!/usr/bin/env python
# His Name Is Willard Game
# Author: Dave Russell (drussell)

import random
import smithjokes

possibleValues = ['Will Smith', 'Willard Smith', 'Will', 'Willard']
wsmith = random.choice(possibleValues)
actor = random.choice(possibleValues)

if (wsmith == actor):
    smithjokes.insertRandomJoke()
else:
    print('His name is Willard!')

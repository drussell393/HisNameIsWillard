#!/usr/bin/env python
# Jokes to go along with the game
# Author: Dave Russell (drussell)

import random

# Adding colours for a sexier terminal
COLOUR = {
    'red': '\033[31m',
    'blue': '\033[34m',
    'reset': '\033[00m'
}

jokes = [
    'July 4th: The day Will Smith saved us from the Aliens.',
    'Will Smith leaves fresh prints in the snow.',
    'Hey Will, is it hard to be a blacksmith?',
    '' + COLOUR['red'] + 'Carlton:' + COLOUR['reset'] +
    ' Will, you get it, you\'re closer. \n'
    '' + COLOUR['blue'] + 'Will:' + COLOUR['reset'] +
    ' Yeah, well you are closer to the floor.',
    'You definitely ain\'t a brother.',
    '' + COLOUR['red'] + 'Carlton:' + COLOUR['reset'] +
    ' Why can\'t you act like an adult? \n'
    '' + COLOUR['blue'] + 'Will:' + COLOUR['reset'] +
    ' Why can\'t you look like one?',
    '' + COLOUR['red'] + 'Carlton:' +
    COLOUR['reset'] + ' Will, you MUST change! \n'
    '' + COLOUR['blue'] + 'Will:' +
    COLOUR['reset'] + 'Carlton, you MUST grow!',
    'Are you gonna be needing a booster seat there little boy?',
    'Daddy, I wanna grow!!!!!',
    'Now this is my brother Carlton. We can\'t afford new clothes, so he just doesn\'t grow!',
    'I went for an interview to be a blacksmith the other day. \n'
    'Apparently dressing up as Will Smith for Halloween doesn\'t count as \"experience\"',
    'WIIIIIIIIIIIIILLLLLLLLL!!!!!!!!',
    'Will Smith is the whitest Will Smith I\'ve ever seen']

# These jokes are courtesy of websites... except the last one... that was
# courtesy of someone in Linode.


def insertRandomJoke():
    print(random.choice(jokes))

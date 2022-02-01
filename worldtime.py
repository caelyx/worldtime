#!/usr/bin/env python3
"""worldtime.py -- show the current time in different cities. 

Highlights Western business hours in green.
See config.py for settings."""

from datetime import datetime
from zoneinfo import ZoneInfo

from config import cities, itemsPerRow, dayStartHour, dayEndHour, workWeek


colors = {
    # With thanks to https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#background-colors
    'reset': u"\u001b[0m", 
    'Black': u"\u001b[40m",
    'Red': u"\u001b[41m",
    'Green': u"\u001b[42m",
    'Yellow': u"\u001b[43m",
    'Blue': u"\u001b[44m",
    'Magenta': u"\u001b[45m",
    'Cyan': u"\u001b[46m",
    'White': u"\u001b[47m",
    }


def main(): 
    now = datetime.now()

    print()
    row = 0

    for name, zone in cities:
        timeval = now.astimezone(ZoneInfo(zone))
        timestr = timeval.strftime("%a %I:%M %p") + colors['reset']
        if timeval.weekday() in workWeek and (timeval.hour >= dayStartHour and timeval.hour < dayEndHour):
            timecolor = colors['Green']
        else:
            timecolor = colors['Black']
        print(f"{timecolor}{name} {timestr}")
        row += 1
        if itemsPerRow and not row % itemsPerRow: 
            print()


if __name__ == '__main__':
    main()

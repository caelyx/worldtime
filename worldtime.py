#!/usr/bin/env python3
"""worldtime.py -- show the current time in different cities. 

Highlights Western business hours in green.
See config.py for settings."""

from datetime import datetime
from zoneinfo import ZoneInfo

from config import cities, itemsPerRow, dayStartHour, dayEndHour, workWeek, display24H


colors = {
    # With thanks to https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#background-colors
    "reset": "\u001b[0m",
    "Black": "\u001b[40m",
    "Red": "\u001b[41m",
    "Green": "\u001b[42m",
    "Yellow": "\u001b[43m",
    "Blue": "\u001b[44m",
    "Magenta": "\u001b[45m",
    "Cyan": "\u001b[46m",
    "White": "\u001b[47m",
}


def main():
    now = datetime.now()

    # Print the header
    print()
    row = 0

    for name, zone in cities:
        timeval = now.astimezone(ZoneInfo(zone))

        if display24H: 
            timestr = timeval.strftime("%H%M %a")
        else:
            timestr = timeval.strftime("%I ") + timeval.strftime("%p ").lower() + timeval.strftime("%a")

        # Check if it's working hours there
        if timeval.hour >= dayStartHour and timeval.hour < dayEndHour:
            if timeval.weekday() in workWeek:
                timecolor = colors["Green"] # Daytime and work week
            else:
                timecolor = colors["Blue"] # Daytime and weekend
        else:
            timecolor = colors["Black"] # Night

        print(f"{timecolor}{name} {timestr}" + colors["reset"])

        # Add a row separator
        row += 1
        if itemsPerRow and not row % itemsPerRow:
            print()


if __name__ == "__main__":
    main()

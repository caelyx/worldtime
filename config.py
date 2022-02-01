#### CONFIG ####

cities = [
        ('SFO', 'America/Los_Angeles'), 
        ('NYC', 'America/New_York'), 
        ('LON', 'Europe/London'),
        ('SG ', 'Asia/Singapore'),
        ('SYD', 'Australia/Sydney'),
        ('AKL', 'Pacific/Auckland')
        ]

itemsPerRow = 2 # Set to False if you don't want row separation

dayStartHour = 8 # 8am start
dayEndHour = 18  # 6pm end
workWeek = [0, 1, 2, 3, 4] # Monday to Friday; see datetime.datetime.weekday()

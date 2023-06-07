from datetime import datetime, timedelta,time

starting_time = datetime.now()

ending_time = starting_time + timedelta(seconds=3690.57)

td = ending_time - starting_time
print(f'Raw td: {td}')

td_sec_rounded = round(td.total_seconds())

# get hours, minutes and seconds:
td_hours = td_sec_rounded//3600
td_minutes = (td_sec_rounded % 3600)//60
td_seconds = td_sec_rounded % 60

print(f'{td_hours:02}:{td_minutes:02}:{td_seconds:02}')

# if we need to create time object
time_from_td = time(hour=td_hours, minute=td_minutes, second=td_seconds)

print(time_from_td.strftime('%H:%M:%S'))

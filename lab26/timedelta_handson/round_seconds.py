from datetime import datetime, timedelta
from time import time, sleep

starting_time = datetime.now()

ending_time = starting_time + timedelta(seconds=3610.57)


final_time = ending_time - starting_time

# final_time_str = str(final_time)
# final_time_list = final_time_str.split('.')
# print(final_time_list[0])


print(final_time.total_seconds())
# # Round the total seconds and convert it to timedelta
rounded_seconds = round(final_time.total_seconds())
rounded_final_time = timedelta(seconds=rounded_seconds)

print(f'Raw final_time: {final_time}')
print(f'Rounded final_time: {rounded_final_time}')

import datetime,time

# now_humman = datetime.datetime.now()
# now_epoch = time.time()

# print(f"now_humman: {now_humman}")
# print(f"now_epoch: {now_epoch}")


# --------------- TASK: get year, day of week, month, hours.... -------------- #
# now = datetime.datetime.now()

# print(now)

# print(f'Current year: {now.year}')
# print(f'Current month: {now.month}')
# print(f'day: {now.day}')
# print(f'week day: {now.weekday()}') # First day of week is 0



### datetime.strptime()

# some_date = datetime.datetime.strptime('13.05.2023T18:06','%d.%m.%YT%H:%M')
# print(some_date)
# print(f'{some_date.day}.{some_date.month}.{some_date.year}, {some_date.hour}')

### datetime.strftime(object)
# now = datetime.datetime.now()
# now_str = now.strftime("%d-%m-%Y")
# print(now_str)

# ----------------------------------- TASK ----------------------------------- #
# Calculate user age as days
# now = datetime.datetime.now()

# # birth_date_str = input('Enter bith date [%d.%m.%Y]:')
# birth_date_str = '13.05.2000'
# birth_date = datetime.datetime.strptime(birth_date_str,'%d.%m.%Y')

# t1 = now - birth_date
# print(t1.days)




# ---------------------- print "END" when 10 sec passed: --------------------- #
# get start time

# print( time.time())
# print( time.time_ns())
# start_time = time.time()

# a = input('Answer:')

# end_time = time.time()
print(f'Your answer takes {round(end_time-start_time, 2)} sec')






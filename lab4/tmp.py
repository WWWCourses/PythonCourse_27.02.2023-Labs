#------------------------This program takes a course lenght in academical hours and corverts them
#into astronomical. It is designed to give a 15 min break for every 3 academical hours that pass.
#declarations

#input
astronomical_hour = 60 # lenght of one astronomical hour in minutes
academical_hour = 45 # lenght of one academical hour in minutes
break_lenght = 15 # lenght of break in minutes
course_lenght=64 # total academical hours
break_interval = 3 # how many academical hours pass before a break

#Operations

total_lenght = academical_hour*course_lenght
total_breaks = (course_lenght//break_interval)*break_lenght
total_astronomical_hours = (total_lenght+total_breaks)/astronomical_hour

#Output

print(f"""The lenght of the course is {total_astronomical_hours} astronomical hours or
 {int(total_astronomical_hours)} astronomical hours and
 {(total_lenght+total_breaks)%astronomical_hour} minutes.""")
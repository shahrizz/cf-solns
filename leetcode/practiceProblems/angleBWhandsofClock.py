hour = 1
minutes = 57
if hour == 12:
    angle_raw_hour = ((hour) * 30) - 360
else:
    angle_raw_hour = (hour) * 30
minute_raw_hour = 6 * minutes
# print(minute_raw_hour)
angle_adjusted_hour = angle_raw_hour + (minutes) * (30) / 60
difference = abs(angle_adjusted_hour - minute_raw_hour)
if difference > 180:
    difference = 360 - difference

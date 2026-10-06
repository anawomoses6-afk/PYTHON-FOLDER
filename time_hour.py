

def seconds_midnight(hour, minute, second):
    seconds_hour = hour * 60 * 60
    seconds_minute = minute * 60
    return seconds_hour + seconds_minute + second


print(seconds_midnight(13, 30, 45))





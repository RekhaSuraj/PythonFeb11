# time module

import time

t1 = time.localtime()
print(t1)

# time.struct_time(tm_year=2025, tm_mon=4, tm_mday=11, tm_hour=10, tm_min=43, tm_sec=29, tm_wday=4, tm_yday=101, tm_isdst=0)

# What does this mean?
# Field	Meaning
# tm_year	Year (e.g. 2025)
# tm_mon	Month (1–12)
# tm_mday	Day of the month (1–31)
# tm_hour	Hour (0–23)
# tm_min	Minute (0–59)
# tm_sec	Second (0–59)
# tm_wday	Weekday (0=Monday)
# tm_yday	Day of the year (1–366)
# tm_isdst	1=Daylight Saving Time, 0=Standard Time

# In a readable format
# print(help(time.strftime))
# %Y  Year with century as a decimal number.
#     %m  Month as a decimal number [01,12].
#     %d  Day of the month as a decimal number [01,31].
#     %H  Hour (24-hour clock) as a decimal number [00,23].
#     %M  Minute as a decimal number [00,59].
#     %S  Second as a decimal number [00,61].
#     %z  Time zone offset from UTC.
#     %a  Locale's abbreviated weekday name.
#     %A  Locale's full weekday name.
#     %b  Locale's abbreviated month name.
#     %B  Locale's full month name.
#     %c  Locale's appropriate date and time representation.
#     %I  Hour (12-hour clock) as a decimal number [01,12].
#     %p  Locale's equivalent of either AM or PM.
#
#     Other codes may be available on your platform.  See documentation for
#     the C library strftime function.

print(time.strftime('%Y-%m-%d %H-%M-%S',t1))
# 2025-04-11 10-56-03
# Have the function CountingMinutes(str) take the str parameter being passed which will be two times (each properly formatted with a colon and
# am or pm) separated by a hyphen and return the total number of minutes between the two times. The time will be in a 12 hour clock format.

import re
def CountingMinutes(strParam):
  def calc_Mins (h, m, am):
    hours = 0
  # Here we just want true if it's either am and not 12 or 12 and pm
    if am != (h == '12'):
      hours += int(h)
   # Here we just want to exclude 12am, which should stay at hours = 0, the default value
    elif h != '12':
      hours += int(h) + 12
    return 60 * hours + int(m)
  
  times = re.findall(r'\d+|am|pm', strParam)
  time1 = calc_Mins(times[0], times[1], times[2] == 'am')
  time2 = calc_Mins(times[3], times[4], times[5] == 'am')
  # If time2 is less than time1, then we calculate minutes that pass if time1 is in day 1 and time2 is in day 2 
  return time2 - time1 if time2 >= time1 else time2 - time1 + 1440

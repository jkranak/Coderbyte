import re
def MostFreeTime(strArr):
  #This converts times to minutes after mindnight
  def minute_convert (h, m, am):
    hours = 0
    if am != (h == '12'):
      hours = int(h)
    elif not am:
      hours = int(h) + 12
    return 60 * hours + int(m)
  
  # We convert events to a list of number lists, including start and end
  event_list = []
  for t in strArr:
    times = re.findall(r'\d+|AM|PM', t)
    start = minute_convert(times[0], times[1], times[2] == 'AM')
    end = minute_convert(times[3], times[4], times[5] == 'AM')
    event_list.append([start, end])
  
  # We sort events by start time
  events = sorted(event_list, key=lambda x: x[0])
  # We calculate all gaps between events
  gaps = list(map(lambda x, y: y[0] - x[1], events[:-1], events[1:]))
  max_gap = max(gaps)
  return '{:>02}:{:>02}'.format(max_gap // 60, max_gap % 60)

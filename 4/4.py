from datetime import datetime
import sys

# part one AHH
class SleepData:

    def __init__(self, start, end, dur):
        self.start = start
        self.end = end
        self.dur = dur

def parse_date(x: str) -> datetime:
    return datetime.strptime(x[x.find('[') + 1:x.find(']')], '%Y-%m-%d %H:%M')

def parse_id(x: str) -> int:
    if '#' not in x:
        return -1
    return x[x.find('#') + 1:x.find(' b')]

def is_asleep(x: str) -> bool:
    return 'asleep' in x

ord_logs = sorted(sys.stdin.readlines(), key=parse_date)

guard_id = -1
last_asleep = -1
sleeps = {}
for l in ord_logs:
    now = parse_date(l).minute
    new_guard = parse_id(l)
    guard_id = new_guard if new_guard != -1 else guard_id
    if new_guard == -1 and not is_asleep(l):
        if guard_id not in sleeps:
            sleeps[guard_id] = [SleepData(last_asleep, now, now - last_asleep)]
        else: sleeps[guard_id].append(SleepData(last_asleep, now, now - last_asleep))
    elif is_asleep(l):
        last_asleep = parse_date(l).minute

def sum_dur(xs: [SleepData]):
    tot = 0
    for x in xs:
        tot += x.dur
    return tot

def max_min(xs: [SleepData]):
    count = [0] * 60
    for x in xs:
        for i in range(x.start, x.end + 1):
            count[i] += 1
    return (count.index(max(count)), max(count))

k = max(sleeps, key=lambda x: sum_dur(sleeps.get(x)))
print('{}: {} minutes asleep, min: {}, check: {}'.format(k, sum_dur(sleeps[k]), max_min(sleeps[k])[0], int(k) * max_min(sleeps[k])[0]))

# part two

k_2 = max(sleeps, key=lambda x: max_min(sleeps.get(x))[1])
print('{}: {} most frequent'.format(k_2, max_min(sleeps[k_2])))

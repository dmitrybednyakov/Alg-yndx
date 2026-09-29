n = int(input())

events = []

for _ in range(n):
    start, end, cost = map(int, input().split())
    events.append((start, cost))
    events.append((end, -cost))

events.sort()

current_load = 0
max_load = 0
max_time = 0

i = 0
while i < len(events):
    time = events[i][0]
    
    while i < len(events) and events[i][0] == time:
        current_load += events[i][1]
        i += 1
    
    if current_load > max_load:
        max_load = current_load
        max_time = time

print(max_load, max_time)
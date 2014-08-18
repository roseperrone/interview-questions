'''
There are at most eight servers in a data center. Each server has got a capacity/memory limit. There can be at most 8 tasks that need to be scheduled on those servers. Each task requires certain capacity/memory to run, and each server can handle multiple tasks as long as the capacity limit is not hit. Write a program to see if all of the given tasks can be scheduled or not on the servers?

Ex:
Servers capacity limits: 8, 16, 8, 32
Tasks capacity needs: 18, 4, 8, 4, 6, 6, 8, 8
For this example, the program should say 'true'.

Ex2:
Server capacity limits: 1, 3
Task capacity needs: 4
For this example, program should return false.
'''

from collections import defaultdict
from copy import copy


# There's a bug in here!
def tasks_for_servers(capacity_limits, capacity_needs, assignments):
  # Check if there are already 8 tasks scheduled to the given server
  if len(capacity_needs) == 0:
    return True
  for i in range(len(capacity_needs)):
    need = capacity_needs[i]
    new_needs = copy(capacity_needs)
    del new_needs[i]
    for j, limit in enumerate(capacity_limits):
      if len(assignments[i]) < 8 and sum(assignments[j]) + need <= limit:
        new_assignments = copy(assignments)
        new_assignments[j].append(need)
        if tasks_for_servers(capacity_limits, copy(new_needs), new_assignments):
          return True
    print need
    print assignments
  return False


print tasks_for_servers([1, 4], [3], defaultdict(list))
print tasks_for_servers([8, 16, 8, 32], [18, 4, 8, 4, 6, 6, 8, 8], defaultdict(list))

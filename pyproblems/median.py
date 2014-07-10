# Find the mathematical median in a list of numbers

data = [3, 6, 20, 99, 10, 15]
data2 = [9, 8, 7, 6, 5]

def median(data):
  data.sort()
  if len(data) % 2 != 0:
    i = len(data)/2
    for a in range(int(i)):
      data.pop()
    data.reverse()
    for b in range(int(i)):
        data.pop()
    return int(data[0])
  else:
    i = len(data)/2 - 1
    for a in range(int(i)):
      data.pop()
    data.reverse()
    for b in range(int(i)):
      data.pop()
    data[0] = float((data[0] + data.pop()))/2
    return data[0]

print median(data)
print median(data2)

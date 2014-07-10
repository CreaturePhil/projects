# Trim an array down to its non-unique elements

arr = [1, 2, 3, 4, 5, 3]

def trimDown(data):
  new = []
  for i in data:
    if data.count(i) > 1:
      new.append(i)

  return new

print trimDown(arr)

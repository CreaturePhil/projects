# Check the strength of your favorite password

def passStrength(data):
  if len(data) < 10:
    return False
  if not any(char.isdigit() for char in data):
    return False
  if not any(char.isupper() for char in data):
    return False
  if not any(char.islower() for char in data):
    return False

  return True

print passStrength('A1213pokl')
print passStrength('1234')
print passStrength('asasasasasasasaas')
print passStrength('bAse730onE4')

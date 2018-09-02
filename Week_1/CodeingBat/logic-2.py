def lone_sum(a, b, c):
  res = 0
  if a != b and a != c:
    res += a
  if b != a and b != c:
    res += b
  if c != a and c != b:
    res += c
  return res

def lucky_sum(a, b, c):
  res = 0
  if a != 13:
    res += a
  else: return 0
  if b != 13:
    res += b
  else: return res
  if c != 13:
    res += c
  else: return res
  return res

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
  if n in range(13, 15) or n in range(17, 20):
    return 0
  return n

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(n):
  if n % 10 == 0:
    return n
  if n % 10 >= 5:
    return (n/10 +1) *10
  elif n % 10 < 5: 
    return (n/10) *10

def close_far(a, b, c):
  if abs(a-b) <=1 and abs(a-c) > 1 and abs(b-c) > 1:
    return True
  elif abs(a-b) > 1 and abs(a-c) <= 1  and abs(b-c) > 1:
    return True
  else:
    return False

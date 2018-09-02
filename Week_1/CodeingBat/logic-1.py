def cigar_party(cigars, is_weekend):
  if is_weekend:
    return True
  elif cigars >= 40 and cigars <= 60:
    return True
  else:
    return False

def date_fashion(you, date):
  if date <= 2 or you <= 2:
    return 0
  elif date >= 8 or you >= 8:
    return 2
  else:
    return 1

def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  return 60 <= temp <= 90

def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
  if speed <= 60:
    return 0
  if 61 <= speed <= 80:
    return 1
  else:
    return 2

def sorta_sum(a, b):
  if a + b >= 10 and a + b <= 19:
    return 20
  return a + b

def alarm_clock(day, vacation):
  week_day = day not in (0, 6)
  if vacation:
    return '10:00' if week_day else 'off'
  return '7:00' if week_day else '10:00'

def love6(a, b):
  if a == 6 or b == 6:
    return True
  if a + b == 6 or abs(a - b) == 6:
    return True
  return False

def in1to10(n, outside_mode):
  if not outside_mode:
    return n in range(1, 11)
  return n not in range(1, 11)

def near_ten(num):
  if num % 10 <= 2 or num % 10 >= 8:
    return True
  return False
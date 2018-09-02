def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  return False
  
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile or not a_smile and not b_smile:
    return True
  return False
  
def sum_double(a, b):
  if a == b:
    return 4 * a
  return a + b

def diff21(n):
  if 21 - n > 0:
    return 21 - n
  return -2 * (21 - n)

def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  return False
  
def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True
  return False
  
def near_hundred(n):
  if (abs(100 - n) <= 10) or (abs(200 - n) <= 10):
    return True
  return False

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return (a < 0 and b > 0) or (a > 0 and b < 0)

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

def missing_char(str, n):
  str1 = str[:n]
  str2 = str[n+1:]
  return str1 + str2

def front_back(str):
  if len(str) <= 1:
    return str
  m = str[1:len(str)-1]
  return str[len(str)-1] + m + str[0]
  
def front3(str):
  t = ""
  for i in range(3):
    t += str[:3]
  return t


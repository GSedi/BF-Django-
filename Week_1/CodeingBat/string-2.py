def double_char(str):
  return ''.join([c+c for c in str])

def count_hi(str):
  res = 0
  for i in range(len(str)-1):
    if str[i:i+2] == "hi":
      res += 1
  return res

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == "cat":
      cat += 1
  for i in range(len(str)-2):
    if str[i:i+3] == "dog":
      dog += 1
  return cat == dog

def count_code(str):
  res = 0
  for i in range(len(str)-3):
    if str[i:i+2] == "co" and str[i+3] == "e":
      res += 1
  return res


def end_other(a, b):
  a.lower()
  b.lower()
  return a in b or b in a

def xyz_there(str):
  if len(str) <3:
    return False
  for i in range(len(str)-2):
    if i > 0:
      if str[i:i+3] == "xyz" and str[i-1] != ".":
        return True
    else:
      if str[i:i+3] == "xyz":
        return True
  return False
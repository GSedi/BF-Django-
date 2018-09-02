def string_times(str, n):
  t = ""
  for i in range(n):
    t += str
  return t

def front_times(str, n):
  if len(str) >= 3:
    s = str[:3]
  else:
    s = str
  t = ""
  for i in range(n):
    t += s
  return t

def string_bits(str):
  t = ""
  for i in range(len(str)):
    if i % 2 == 0:
      t += str[i]
  return t

def string_splosion(str):
  t = ""
  for i in range(len(str)+1):
    t += str[:i]
  return t

def last2(str):
  if len(str) < 2:
    return 0
  res = 0
  comp = str[len(str)-2] + str[len(str)-1]
  for i in range(len(str)-2):
    temp = str[i] + str[i+1]
    if temp == comp:
      res += 1
  return res

def array_count9(nums):
  res = 0
  for i in nums:
    if i == 9:
      res += 1
  return res

def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count


""" Warmup-1 - 10/21"""
def sleep_in(weekday, vacation):
  return not weekday or vacation
  # if not weekday or vacation:
  #   return True
  # else:
  #   return False


def diff21(n):
  if n > 21:
    return abs(n - 21) * 2
  else:
    return abs(n - 21)


def near_hundred(n):
  return (abs(100-n) <= 10) or (abs(200-n) <= 10)


def missing_char(str, n):
  front = str[:n]
  back  = str[n+1:]
  return front + back




""" List-1 - 10/22"""
def first_last6(nums):
  isFirst = nums[0] == 6
  isLast  = nums[len(nums) - 1] == 6
  if isFirst or isLast:
    return True
  else:
    return False
  # return isFirst or isLast


def common_end(a, b):
  sameFirst = a[0] == b[0]
  sameLast = a[-1] == b[-1]
  return sameFirst or sameLast


def reverse3(nums):
  # rev = [nums[2], nums[1], nums[0]]
  rev = []
  rev.append(nums[2])
  rev.append(nums[1])
  rev.append(nums[0])
  return rev


def middle_way(a, b):
  midA = a[1]
  midBIndex = len(b)//2  # int(round(len(b)/2))
  midB = b[midBIndex]
  return [midA, midB]




""" Logic-1 - 10/8 """
def cigar_party(cigars, is_weekend):
  if is_weekend:
    # return cigars >= 40
    if cigars >= 40:
      return True
  else:
    if cigars >= 40 and cigars <= 60:
      return True
  return False


def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed <= 60:
      return 0
    elif speed > 60 and speed <= 80:
      return 1
    else:
      return 2
  elif speed <= 65:
    return 0
  elif speed > 65 and speed <= 85:
    return 1
  else:
    return 2


def love6(a, b):
  if a == 6 or b == 6:
    return True
  Sum = a + b
  diff = abs(a - b)
  # return Sum == 6 or diff == 6
  if Sum == 6 or diff == 6:
    return True
  return False

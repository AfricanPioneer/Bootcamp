def find_missing(list_a, list_b):
  if len(list_a) == 0 and len(list_b) == 0:#Compares both lists length to determine if they are empty
    return 0
  elif len(list_a) == len(list_b):#Compares both lists length to determine if they are of equal length
    for num in list_a:
      if num in list_b:
        return 0
  else:
    if len(list_a) < len(list_b):#Compares both lists length to determine if they have the same number of values
      for num in list_b:
        if num not in list_a:
          return num # if not it returns the extra number in the list


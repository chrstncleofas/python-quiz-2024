# Given a list that contains strings, integers and booleans, write a function that:
# 1. Converts all boolean to string
# 2. Converts all integers to string
# 3. Converts all strings to uppercase
# 4. Removes all strings that contain the letter "a"
# 5. Returns the list

def manipulate_list(lst: list) -> list:

  rt = []
  for i in lst:
    if type(i) == bool:
      rt.append(str(i))
    elif type(i) == int:
      rt.append(str(i))
    elif 'a' in i:
      continue
    else:
      rt.append(i.upper())
  return rt

lst = [True, False, 12, 19, "Test String", "Christian"]

print(manipulate_list(lst))

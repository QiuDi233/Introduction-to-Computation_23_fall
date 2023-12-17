import re
n = input()
n = re.sub(r'\s+', ' ', n)
print(n)
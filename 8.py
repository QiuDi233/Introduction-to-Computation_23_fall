try:
  while True:
        x=input()
        if not x:
            break
        num = 0
        while x == x[::-1] and len(x) >= 2:
            num += 1
            if len(x) % 2 == 0:
                x = x[:int(len(x) / 2)]
            else:
                x = x[:int((len(x) - 1) / 2)]
        print(num)
except:
    pass
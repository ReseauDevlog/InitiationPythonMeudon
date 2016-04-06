def linspace(begin, end, n):
  step = (end - begin)/(n-1)
  for i in range(n):
    print(begin + i*step)

linspace(0,1,10)

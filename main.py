

import time

f1 = 1
f2 = f1

while True:
  f1, f2 = f2, f1 + f2
  
  print(f2)

  #time.sleep(0.5)
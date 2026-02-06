import time

for i in range(3):
 if i == 1:
  print('*'*53)
 else:
   print("*"*50)

for z in range(20):
 if z == 1:
  time.sleep(0.1)
 else:
  
  print(' '*z + '*'*z)
import time

i = 0
while True:
    print('*', end='')
    i += 1
    if i == 1000:
        break
    time.sleep(0.1)

import subprocess
import time

for i in range(1000000000):
    print('Try {}'.format(i))
    ret = subprocess.call('git push -u origin main')
    print(ret)
    if ret == 0:
        break

    time.sleep(1)

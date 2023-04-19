import os
import time

l = []
result = os.fork()

if result == 0:
    print("I am main process")
    l.append(5)
else:
    print(f"I am new! {os.getpid()} {result}")
    l.append(4)

print(l)
time.sleep(40)
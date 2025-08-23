## Importing modules:

from concurrent.futures import ProcessPoolExecutor
import time


def sq_num(i):
    time.sleep(1)
    return f"Number is :{i*i}"


input = [1, 2, 3, 4, 5, 6]  ## Input list.

t = time.time()  ## Start time.

with ProcessPoolExecutor(max_workers=6) as executor:  ## No of processes = 6.
    results = executor.map(sq_num, input)

for result in results:
    print(result)

print(f"Time taken:{time.time()-t}")

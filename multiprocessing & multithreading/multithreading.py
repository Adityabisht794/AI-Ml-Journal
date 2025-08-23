## importing modules:

import multiprocessing
import time


def sq_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i}:{i*i}")


def cube_num():
    for i in range(5):
        time.sleep(1)
        print(f"Cube of {i}:{i*i*i}")


if __name__ == "__main__":  ## Prevents infinite process swapping.

    ## Creation of processes:
    p1 = multiprocessing.Process(target=sq_num)
    p2 = multiprocessing.Process(target=cube_num)

    t = time.time()

    ## Staring processes:
    p1.start()
    p2.start()

    ## After Executoin:
    p1.join()
    p2.join()

    finish_time = time.time() - t
    print("Time-taken:", finish_time)

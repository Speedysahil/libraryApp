import time
from functools import lru_cache
@lru_cache(15)
def delaytime(n):
    time.sleep(n)
    return(n)

def somework():
    print("some work is doing here")
    delaytime(3)
    print("it taking so long")
    delaytime(5)
    delaytime(1)
    delaytime(2)
    delaytime(3)
    print("it took 10 second to reach me")
    delaytime(1)
    delaytime(2)
    delaytime(3)
    print("it will print in instant")

somework()
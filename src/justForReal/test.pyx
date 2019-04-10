import time
import numpy as np

start_time = time.time()
a = np.random.rand(100, 100) * 2 - 1
b = np.random.rand(100, 100) * 2 - 1

for i in range(500000):
    c = a + b
    c = a * b

end_time = time.time()
print(end_time - start_time)

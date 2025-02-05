import numpy as np
import time

start_time = time.perf_counter()

total = np.sum(np.arange(1_000_000))

end_time = time.perf_counter()
print(f"Execution Time: {end_time - start_time} seconds")

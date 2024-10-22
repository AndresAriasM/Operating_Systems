from multiprocessing import Pool
import time

def cube(number):
    return number * number * number

numbers = range(100)
pool = Pool(24)

start = time.time()
result = pool.map(cube, numbers)

pool.close()
pool.join()

print(result, "tiempo total para la ejecución: ", time.time()-start)

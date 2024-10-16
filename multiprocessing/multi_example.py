import multiprocessing
import multiprocessing.process
import time

def contar(num):
    cnt = 0
    for _ in range(num):
        cnt += 1
        time.sleep(0.1)
    print("Contador terminó")

#ejecución serial
#Se demorará la suma de todos los tiempos individuales (0.5+1+2.5+3)
start = time.time()
contar(5)
contar(10)
contar(25)
contar(30)
print("Tiempo de ejecución serial", time.time()-start)

#ejecución con multiprocesamiento
#Se demorará el tiempo máximo dentro de los procesos incluidos (3 segundos)
start = time.time()
p1 = multiprocessing.Process(target=contar, args=[5])
p2 = multiprocessing.Process(target=contar, args=[10])
p3 = multiprocessing.Process(target=contar, args=[25])
p4 = multiprocessing.Process(target=contar, args=[30])

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

print("Tiempo de ejecución paralelo", time.time()-start)
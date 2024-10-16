from multiprocessing import Queue, Process

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(i*-1)

def add_10(numbers, queue):
    for i in numbers:
        queue.put(i+10)
        
def divide_by_2(numbers, queue):
    for i in numbers:
        queue.put(i/2)

def power_of_3(numbers, queue):
    for i in numbers:
        queue.put(i**3)
    

q = Queue()
numbers = range(1,5)

p1 = Process(target=square, args=[numbers, q])
p2 = Process(target=make_negative, args=[numbers, q])
p3 = Process(target=add_10, args=[numbers, q])
p4 = Process(target=divide_by_2, args=[numbers, q])
p5 = Process(target=power_of_3, args=[numbers, q])

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()

while not q.empty():
    print(q.get())
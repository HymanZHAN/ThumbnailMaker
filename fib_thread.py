import threading

class FibonacciThread(threading.Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        fib=[0] * (self.num+1)
        fib[0] = 0
        fib[1] = 1
        for i in rang(2, self.num+1):
            fib[i] = fib[i-1] + fib[i-2]
            print(fib[self.num]

fib_task_one = FibonacciThread(9)
fib_task_two = FibonacciThread(12)

fib_task_one.start()
fib_task_two.start()

fib_task_one.join()
fib_task_two.join()
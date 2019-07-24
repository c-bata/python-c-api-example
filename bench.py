import time
import fibonacci
import pyfibonacci
import cyfibonacci

from concurrent.futures import ThreadPoolExecutor, wait


def bench(callable, *args, **kwargs):
    task_num = kwargs.get('task_num', 20)

    start = time.time()
    with ThreadPoolExecutor(4) as pool:
        futures = [pool.submit(callable, *args, **kwargs) for _ in range(task_num)]
        wait(futures)
        elapsed = time.time() - start
        print(f"{elapsed / task_num:.6f} s/op")


def main():
    n = 30
    print("Python")
    bench(pyfibonacci.fibonacci, n)

    print("C Extension with gil")
    bench(fibonacci.fibonacci, n)

    print("C Extension with nogil")
    bench(fibonacci.fibonacci, n, nogil=True)

    print("Cython")
    bench(cyfibonacci.fibonacci, n)


if __name__ == '__main__':
    main()

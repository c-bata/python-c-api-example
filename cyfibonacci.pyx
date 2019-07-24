def fibonacci(unsigned int n):
    cdef long long result
    with nogil:
        result = fibonacci_cc(n)
    return result

cdef long long fibonacci_cc(unsigned int n) nogil:
    if n < 2:
        return 1
    else:
        return fibonacci_cc(n-1) + fibonacci_cc(n-2)

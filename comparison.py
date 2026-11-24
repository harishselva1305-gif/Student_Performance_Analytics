import numpy as np
import time
import sys


def compare_addition():

    print("\n--- ADDITION COMPARISON ---")

    python_list = [10, 20, 30, 40, 50]

    numpy_array = np.array([10, 20, 30, 40, 50])

    list_result = [x + 5 for x in python_list]

    array_result = numpy_array + 5

    print("Python List Result:", list_result)

    print("NumPy Array Result:", array_result)


def compare_multiplication():

    print("\n--- MULTIPLICATION COMPARISON ---")

    python_list = [10, 20, 30, 40, 50]

    numpy_array = np.array([10, 20, 30, 40, 50])

    list_result = [x * 2 for x in python_list]

    array_result = numpy_array * 2

    print("Python List Result:", list_result)

    print("NumPy Array Result:", array_result)


def compare_execution_time():

    print("\n--- EXECUTION TIME COMPARISON ---")

    size = 1000000

    python_list = list(range(size))

    numpy_array = np.arange(size)

    start = time.perf_counter()

    list_result = [x * 2 for x in python_list]

    list_time = time.perf_counter() - start

    start = time.perf_counter()

    array_result = numpy_array * 2

    numpy_time = time.perf_counter() - start

    print("Python List Time:", list_time)

    print("NumPy Array Time:", numpy_time)


def compare_memory_usage():

    print("\n--- MEMORY USAGE COMPARISON ---")

    python_list = list(range(1000))

    numpy_array = np.arange(1000)

    list_memory = sys.getsizeof(python_list) + sum(
        sys.getsizeof(x) for x in python_list
    )

    numpy_memory = numpy_array.nbytes

    print("Python List Memory:", list_memory, "bytes")

    print("NumPy Array Memory:", numpy_memory, "bytes")
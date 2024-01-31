#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import timeit
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(A):
    for i in range(1, len(A)):
        item = A[i]
        k = i
        while k > 0 and A[k - 1] > item:
            A[k] = A[k - 1]
            k -= 1
        A[k] = item

# Benchmarking function
def benchmark_insertion_sort(input_sizes):
    runtimes = []

    for size in input_sizes:
        # Generate a random array of size 'size'
        A = np.random.randint(-1000, 1000, size=size)

        # Measure the execution time
        runtime = timeit.timeit(lambda: insertion_sort(A.copy()), number=1)

        runtimes.append(runtime)

    return runtimes

if __name__ == "__main__":
    # Define input sizes
    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]

    # Benchmark insertion sort
    insertion_sort_runtimes = benchmark_insertion_sort(input_sizes)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, insertion_sort_runtimes, marker='o', color='b', label='Insertion Sort')

    plt.title('Insertion Sort Runtime Analysis')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


# In[5]:


import timeit
import matplotlib.pyplot as plt
import numpy as np

def selection_sort(A):
    num = len(A)
    for i in range(num - 1):
        selection = i
        for j in range(i + 1, num):
            if A[j] < A[selection]:
                selection = j
        A[selection], A[i] = A[i], A[selection]

# Benchmarking function for selection sort
def benchmark_selection_sort(input_sizes):
    runtimes = []

    for size in input_sizes:
        # Generate a random array of size 'size'
        A = np.random.randint(-1000, 1000, size=size)

        # Measure the execution time
        runtime = timeit.timeit(lambda: selection_sort(A.copy()), number=1)

        runtimes.append(runtime)

    return runtimes

if __name__ == "__main__":
    # Define input sizes
    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]

    # Benchmark selection sort
    selection_sort_runtimes = benchmark_selection_sort(input_sizes)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, selection_sort_runtimes, marker='o', color='r', label='Selection Sort')

    plt.title('Selection Sort Runtime Analysis')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

    


# In[6]:


import timeit
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(A):
    n = len(A)
    for j in range(n):
        bubble_found = False
        for i in range(n - 1, j, -1):
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]
                bubble_found = True
        if not bubble_found:
            break

# Benchmarking function for bubble sort
def benchmark_bubble_sort(input_sizes):
    runtimes = []

    for size in input_sizes:
        # Generate a random array of size 'size'
        A = np.random.randint(-1000, 1000, size=size)

        # Measure the execution time
        runtime = timeit.timeit(lambda: bubble_sort(A.copy()), number=1)

        runtimes.append(runtime)

    return runtimes

if __name__ == "__main__":
    # Define input sizes
    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]

    # Benchmark bubble sort
    bubble_sort_runtimes = benchmark_bubble_sort(input_sizes)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, bubble_sort_runtimes, marker='o', color='g', label='Bubble Sort')

    plt.title('Bubble Sort Runtime Analysis')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


# In[ ]:





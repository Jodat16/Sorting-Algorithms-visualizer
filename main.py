import numpy as np 
import time 
import random
from tkinter import ttk, messagebox
from generateColor import getColor
from tkinter import *

speed = 10
def set_slow():
    global speed
    speed = 10

def set_fast():
    global speed
    speed = 100

def display(n, array, color): 
    __canvas.delete('all') 
    width = 1560/(3*n-1) 
    gap = width/2
    for i in range(n): 
        __canvas.create_text(20+i*width+i*gap, 490, text=str(array[i]))
        __canvas.create_rectangle(10+i*width+i*gap, 480-(array[i]/4), 10 + (i+1)*width+i*gap, 480, fill=color[i], tags= str(array[i])) 
    root.update_idletasks()

def merge_sort(arr, left, right):
    if left < right:
        m = (left+right)//2
        merge_sort(arr, left, m)
        merge_sort(arr, m+1, right)
        j = m+1
        if arr[m] <= arr[m+1]:
            return
        while left <= m and j <= right:
            display(N, arr, ['red' if x == left or x == j else 'pink' for x in range(N)])
            time.sleep(1/speed)
            if arr[left] <= arr[j]:
                left += 1
            else:
                display(N, arr, ['cyan' if x == left or x == j else 'pink' for x in range(N)])
                time.sleep(1/speed)
                temp = arr[j]
                i = j
                while i != left:
                    arr[i] = arr[i-1]
                    display(N, arr, ['cyan' if x == i or x == j else 'pink' for x in range(N)])
                    time.sleep(1/speed)
                    i -= 1       
                arr[left] = temp
                display(N, arr, ['green' if x == left or x == j else 'pink' for x in range(N)])
                time.sleep(1/speed)
                left += 1
                m += 1
                j += 1
    display(N, array, ['yellow' for _ in range(N)]) 

def heapify(data, n, i, display):
    display(n, data, ['cyan' if x==i else 'pink' for x in range(n)])
    time.sleep(1/speed) 
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and data[i] < data[left]:
        largest = left
    if right < n and data[largest] < data[right]:
        largest = right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest, display)

def heap_sort(data, display):
    n = len(data)
    for i in range(n//2, -1, -1):
        heapify(data, n, i, display)
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0, display)
        display(n, data, ['green' if x > i else 'cyan' if x==i else 'pink' for x in range(n)])
        time.sleep(1/speed) 
    display(N, array, ['yellow' for _ in range(N)]) 

def partition(data, head, tail, display):
    border = head
    pivot = data[tail] 
    display(N, data, getColor(len(data), head, tail, border, border))
    time.sleep(1/speed)
    for j in range(head, tail):
        if data[j] < pivot:
            display(N, data, getColor(len(data), head, tail, border, j, True))
            time.sleep(1/speed)
            data[border], data[j] = data[j], data[border]
            border += 1
        display(N, data, getColor(len(data), head, tail, border, j))
        time.sleep(1/speed)
    display(N, data, getColor(len(data), head, tail, border, tail, True))
    time.sleep(1/speed)
    data[border], data[tail] = data[tail], data[border]
    return border

def radix_sort():
    maximum = max(array)
    exponent = 1
    while maximum/exponent > 1:
        Radix_count(exponent)
        exponent *= 10

def quick_sort(data, head, tail, display):
    if head < tail:
        partition1 = partition(data, head, tail, display)
        quick_sort(data, head, partition1-1, display)
        quick_sort(data, partition1+1, tail, display)
    display(N, array, ['yellow' for _ in range(N)])    

def counting_sort():
    maximum = 0
    for i in range(N):
        display(N, array, ['green' if x == i else ['cyan'] for x in range(N)])
        time.sleep(1/speed)
        if array[i] > maximum:
            maximum = array[i]
    buckets = [0 for i in range(maximum + 1)]
    for i in array:
        buckets[i] += 1
    i = 0
    for j in range(maximum + 1):
        for _ in range(buckets[j]):
            array[i] = j
            i += 1
            display(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
            time.sleep(1/speed)

def Radix_count(exp):
    output = [0] * (N)
    count = [0] * (10)
    for i in range(0, N):
        index = (array[i]/exp)
        count[int((index)%10)] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = N-1
    while i>=0:
        index = (array[i]/exp)
        output[ count[ int((index)%10) ] - 1] = array[i]
        count[int((index)%10)] -= 1
        i -= 1
        display(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
    i = 0
    for i in range(0,len(array)):
        array[i] = output[i]
        display(N, array, ['green' if x == i else ['cyan'] for x in range(N)])
        time.sleep(1/speed)
    
def bucket_sort():
    largest = max(array)
    size = largest/N
    buckets = [[] for i in range(N)]  
    for i in range(N):
        index = int(array[i]/size)
        if index != N:
            buckets[index].append(array[i])
            display(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
            time.sleep(1/speed)
        else:
            buckets[N - 1].append(array[i])
            display(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
            time.sleep(1/speed)
    for i in range(N):
        buckets[i] = sorted(buckets[i])
        display(N, array, ['cyan' if x==i else 'pink' for x in range(N)])
        time.sleep(1/speed)
        result = []
    for i in range(N):
        result = result + buckets[i]
        time.sleep(1/speed)
    return result
 
def Arrayshuffle(): 
    # to shuffle the array
    np.random.shuffle(array) 
    display(N, array, colors) 

def quick_sort_for_4_7_5(arr, low, high):
    if low<high:
        pivot = partition_for_4_7_5(arr, low, high)
        quick_sort_for_4_7_5(arr, low, pivot-1)
        quick_sort_for_4_7_5(arr, pivot + 1, high)
        return arr

def insertion_sort_for_4_7_5(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        display(N, array, ['yellow' if a == i or a == i +
                               1 else 'green' if a <= j 
                               else'cyan' for a in range(N)])
        time.sleep(1/speed)
        while j>low and arr[j-1]>val:
            arr[j]= arr[j-1]
            display(n, array, ['pink' if a == i else 'green' if a <= j  else'cyan' for a in range(N)]) 
            time.sleep(1/speed)
            j-= 1
        arr[j]= val
 
# Partition function for quicksort
def partition_for_4_7_5(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i]<pivot:
            display(N, arr, getColor(len(arr), low, high, i, j, True))
            time.sleep(1/speed)
            arr[i], arr[j]= arr[j], arr[i]
            j+= 1
    arr[j], arr[high]= arr[high], arr[j]
    return j
 
 
# Hybrid function -> Quick + Insertion sort
def for_4_7_5(arr, low, high):
    while low<high:
 
        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        if high-low + 1<10:
            insertion_sort_for_4_7_5(arr, low, high)
            break
 
        else:
            pivot = partition_for_4_7_5(arr, low, high)
 
            # Optimised quicksort which works on
            # the smaller arrays first
 
            # If the left side of the pivot
            # is less than right, sort left part
            # and move to the right part of the array
            if pivot-low<high-pivot:
                for_4_7_5(arr, low, pivot-1)
                low = pivot + 1
            else:
                # If the right side of pivot is less
                # than left, sort right side and
                # move to the left side
                for_4_7_5(arr, pivot + 1, high)
                high = pivot-1

def for_8_2_4(array,max):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * (max+1)

    # Store the count of each elements in count array
    for i in range(0, size):
        display(N, array, ['green' if x == i else ['cyan'] for x in range(N)])
        time.sleep(1/speed)
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, max+1):
        count[i] += count[i - 1]
#take input a and b from user if possible
#both a and b sould be less than the max element of array
    a=20
    b=35
    c=count[b]-count[a-1]
    print(c)
    
    #for sorting array
    
    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        display(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
        time.sleep(1/speed)
        array[i] = output[i]

def bubble(): 
    if algos['bubble'] is False: 
        algos['bubble'] = True
        bubble_button.config(style='success.TButton') 
        algos['insertion'] = False
        algos['merge'] = False
        algos['heap'] = False
        algos['quick'] = False
        algos['radix'] = False
        algos['bucket'] = False
        algos['counting'] = False
        algos['7_4_5'] = False
        algos['8_2_4'] = False
    else: 
        algos['bubble'] = False
        bubble_button.config(style='danger.TButton') 

def insertion(): 
    if algos['insertion'] is False: 
        algos['insertion'] = True
        insertion_button.config(style='success.TButton') 
        algos['bubble'] = False
        algos['merge'] = False
        algos['heap'] = False
        algos['quick'] = False
        algos['radix'] = False
        algos['bucket'] = False
        algos['counting'] = False
        algos['7_4_5'] = False
        algos['8_2_4'] = False
    else: 
        algos['insertion'] = False
        insertion_button.config(style='danger.TButton')

def merge(): 
    if algos['merge'] is False: 
        algos['merge'] = True
        merge_button.config(style='success.TButton') 
        algos['bubble'] = False
        algos['insertion'] = False
        algos['heap'] = False
        algos['quick'] = False
        algos['radix'] = False
        algos['bucket'] = False
        algos['counting'] = False
        algos['7_4_5'] = False
        algos['8_2_4'] = False
    else: 
        algos['merge'] = False
        merge_button.config(style='danger.TButton')  

def heap(): 
    if algos['heap'] is False: 
        algos['heap'] = True
        heap_button.config(style='success.TButton')
        algos['bubble'] = False
        algos['merge'] = False
        algos['insertion'] = False
        algos['quick'] = False
        algos['radix'] = False
        algos['bucket'] = False
        algos['counting'] = False
        algos['7_4_5'] = False
        algos['8_2_4'] = False
    else: 
        algos['heap'] = False
        heap_button.config(style='danger.TButton')

def quick(): 
    if algos['quick'] is False: 
        algos['quick'] = True
        quick_button.config(style='success.TButton') 
        algos['bubble'] = False
        algos['merge'] = False
        algos['heap'] = False
        algos['insertion'] = False
        algos['radix'] = False
        algos['bucket'] = False
        algos['counting'] = False
        algos['7_4_5'] = False
        algos['8_2_4'] = False
    else: 
        algos['quick'] = False
        quick_button.config(style='danger.TButton')

def radix(): 
    if algos['radix'] is False: 
        algos['radix'] = True
        radix_button.config(style='success.TButton') 
        algos['bubble'] = False
        algos['merge'] = False
        algos['heap'] = False
        algos['quick'] = False
        algos['insertion'] = False
        algos['bucket'] = False
        algos['counting'] = False
        algos['7_4_5'] = False
        algos['8_2_4'] = False
    else: 
        algos['radix'] = False
        radix_button.config(style='danger.TButton')

def bucket(): 
    if algos['bucket'] is False: 
        algos['bucket'] = True
        bubble_button.config(style='success.TButton') 
        algos['bubble'] = False
        algos['merge'] = False
        algos['heap'] = False
        algos['quick'] = False
        algos['radix'] = False
        algos['insertion'] = False
        algos['counting'] = False
        algos['7_4_5'] = False
        algos['8_2_4'] = False
    else: 
        algos['bucket'] = False
        bubble_button.config(style='danger.TButton')

def counting(): 
    if algos['counting'] is False: 
        algos['counting'] = True
        counting_button.config(style='success.TButton') 
        algos['bubble'] = False
        algos['merge'] = False
        algos['heap'] = False
        algos['quick'] = False
        algos['radix'] = False
        algos['bucket'] = False
        algos['insertion'] = False
        algos['7_4_5'] = False
        algos['8_2_4'] = False
    else: 
        algos['countiing'] = False
        counting_button.config(style='danger.TButton')

def _7_4_5(): 
    if algos['7_4_5'] is False: 
        algos['7_4_5'] = True
        _7_4_5_button.config(style='success.TButton') 
        algos['bubble'] = False
        algos['merge'] = False
        algos['heap'] = False
        algos['quick'] = False
        algos['radix'] = False
        algos['bucket'] = False
        algos['insertion'] = False
        algos['counting'] = False
        algos['8_2_4'] = False
    else: 
        algos['7_4_5'] = False
        _7_4_5_button.config(style='danger.TButton')

def _8_2_4(): 
    if algos['8_2_4'] is False: 
        algos['8_2_4'] = True
        _8_2_4_button.config(style='success.TButton') 
        algos['bubble'] = False
        algos['merge'] = False
        algos['heap'] = False
        algos['quick'] = False
        algos['radix'] = False
        algos['bucket'] = False
        algos['insertion'] = False
        algos['counting'] = False
        algos['7_4_5'] = False
    else: 
        algos['8_2_4'] = False
        _8_2_4_button.config(style='danger.TButton')

def run_main():
    if algos['insertion'] == True:
        begin = time.time()
        for j in range(1, len(array)): 
            key = array[j] 
            i = j-1
            display(N, array, ['yellow' if a == i or a == i +
                               1 else 'green' if a <= j 
                               else'cyan' for a in range(N)]) 
            time.sleep(1/speed) 
            while i >= 0 and array[i] > key: 
                array[i+1] = array[i] 
                display(N, array, ['pink' if a == i else 'green' if a <= j  else'cyan' for a in range(N)]) 
                time.sleep(1/speed) 
                i -= 1
            array[i+1] = key
        end = time.time()
        display(N, array, ['yellow' for _ in range(N)])
        messagebox.showinfo("Time Taken: ", str(end - begin) + " seconds")
    elif algos['bubble'] == True:
        begin = time.time()
        for i in range(N):
            time.sleep(1/speed) 
            for j in range(0, N-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    display(N, array, ['pink' if a == i else 'green' if a <= j  else'cyan' for a in range(N)])
        end = time.time()
        display(N, array, ['yellow' for _ in range(N)]) 
        messagebox.showinfo("Time Taken: ", str(end - begin) + "seconds")
    elif algos['merge'] == True:
        begin = time.time()
        merge_sort(array, 0, N - 1)
        end = time.time()
        messagebox.showinfo("Time Taken: ", str(end - begin) + "seconds")
    elif algos['heap'] == True:
        begin = time.time()
        heap_sort(array, display)
        end = time.time()
        messagebox.showinfo("Time Taken: ", str(end - begin) + "seconds")
    elif algos['quick'] == True:
        begin = time.time()    
        quick_sort(array, 0, N-1, display)
        end = time.time()
        messagebox.showinfo("Time Taken: ", str(end - begin) + "seconds")
    elif algos['radix'] == True:
        begin = time.time()   
        radix_sort()
        end = time.time()
        display(N, array, ['yellow' for _ in range(N)]) 
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds") 
    elif algos['bucket'] == True:
        begin = time.time() 
        display(N, bucket_sort(), ['yellow' for x in range(N)])
        end = time.time()
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds")
    elif algos['counting'] == True:
        begin = time.time() 
        counting_sort()
        end = time.time()
        display(N, array, ['yellow' for x in range(N)])
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds")
    elif algos['7_4_5'] == True:
        begin = time.time()
        for_4_7_5(array, 0,len(array)-1)
        print(array)
        display(N,array, ['yellow' for _ in range(N)])
        end = time.time()
        messagebox.showinfo("Time Taken: ", str(end - begin) + "seconds")
    elif algos['8_2_4'] == True:
        begin = time.time()
        maximum = max(array)
        for_8_2_4(array,maximum)
        print(array)
        display(N,array, ['yellow' for _ in range(N)])
        end = time.time()
        messagebox.showinfo("Time Taken: ", str(end - begin) + "seconds")
    else: 
        messagebox.showerror("Algorithm Visualizer", "You need to select a sorting algorithm")

fptr = open("ArrayNumbers.txt", "r" )
array = []
array = list(map(int, fptr.read().split()))
fptr.close()
N = len(array)
print(array)

if __name__ == '__main__': 
    root = ttk.Style().master
    algos = {'insertion': False, 'bubble': False, 'merge': False, 'heap': False, 'quick': False, 'radix': False, 'bucket':False, 'counting': False, '7_4_5':False, '8_2_4':False} 
    root.title('Sorting') 
    root.resizable() 

    colors = ['blue' for _ in range(N)] 
    __canvas = Canvas(root, width=1000, height=500) 
    __canvas.grid(row=500, column=0, columnspan=8) 
    Arrayshuffle() 
    display(N, array, colors)

    Label(root, text='Select the Sorting Algorithm').grid(row=501 ,column=0, columnspan=8) 
    insertion_button = ttk.Button(root, text='Insertion sort', width=14, padding=1, command=insertion) 
    insertion_button.grid(row=502, column=0, padx= 1,  pady=8) 
    bubble_button = ttk.Button(root, text='Bubble sort', width=14, padding=1, command=bubble) 
    bubble_button.grid(row=502, column=1, padx= 1, pady=8)
    merge_button = ttk.Button(root, text='Merge sort', width=14, padding=1, command=merge) 
    merge_button.grid(row=502, column=2, padx= 1,pady=8) 
    heap_button = ttk.Button(root, text='Heap sort', width=14, padding=1, command=heap) 
    heap_button.grid(row=502, column=3, padx= 1,pady=8)
    quick_button = ttk.Button(root, text='Quick sort', width=14, padding=1, command=quick) 
    quick_button.grid(row=502, column=4, padx= 1,pady=8)  
    radix_button = ttk.Button(root, text='Radix sort', width=14, padding=1, command=radix) 
    radix_button.grid(row=502, column=5,padx= 1, pady=8)
    bucket_button = ttk.Button(root, text='Bucket sort', width=14, padding=1, command=bucket) 
    bucket_button.grid(row=502, column=6, padx= 1,pady=8)
    counting_button = ttk.Button(root, text='Counting sort', width=14, padding=1, command=counting) 
    counting_button.grid(row=502, column=7,padx= 1, pady=8)
    _7_4_5_button = ttk.Button(root, text='7_4_5', width=14, padding=1, command=_7_4_5) 
    _7_4_5_button.grid(row=503, column=0, padx= 1,pady=8)
    _8_2_4_button = ttk.Button(root, text='8_2_4', width=14, padding=1, command=_8_2_4) 
    _8_2_4_button.grid(row=503, column=1, padx= 1,pady=8)
    run_main_button = ttk.Button(root, text='Start', width=14, padding=5, command=run_main)  
    run_main_button.grid(row=504, column=3, padx= 10,pady=8)
    shuffle_button = ttk.Button(root, text='Shuffle Array', width=14, padding=5, command=Arrayshuffle) 
    shuffle_button.grid(row=504, column=4,padx= 10, pady=8)

    __slow = ttk.Button(root, text='Slow', padding=5, command=set_slow)
    __slow.grid(row=505, column=3,padx= 10, pady=8)
    __fast = ttk.Button(root, text='Fast', padding=5, command=set_fast)
    __fast.grid(row=505, column=4,padx= 10, pady=8)

    root.mainloop() 
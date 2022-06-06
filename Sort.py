import time
from tkinter import *


# Bubble Sort
def BubbleSort(data, drawdata, speed):
    start_time = time.time()
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawdata(data, ["#dd4124" if x == j + 1 else "#7fcdcd" for x in range(len(data))])
                time.sleep(speed)
    end_time = time.time()
    end_time = int(end_time - start_time)
    color = ["#7fcdcd" for _ in range(len(data))]
    for i in range(len(data)):
        time.sleep(0.01)
        color.insert(i, "#32de84")
        drawdata(data, color)
    return end_time


# insertion sort
def InsertionSort(data, drawdata, speed):
    start_time = time.time()
    for i in range(len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            drawdata(data, ["#dd4124" if x == j + 1 else "#7fcdcd" for x in range(len(data))])
        time.sleep(speed)
        data[j + 1] = key
    end_time = time.time()
    end_time = int(end_time - start_time)
    color = ["#7fcdcd" for _ in range(len(data))]
    for i in range(len(data)):
        time.sleep(0.01)
        color.insert(i, "#32de84")
        drawdata(data, color)
    return end_time


# radix sort
def RadixSort(data, drawdata, speed):
    start_time = time.time()
    max1 = max(data)
    exp = 1
    c = 0
    while max1 / exp > 0:
        c += 1
        n = len(data)
        output = [0] * (n)
        count = [0] * (10)
        for i in range(0, n):
            index = data[i] // exp
            count[int(index % 10)] += 1
            drawdata(data, ["#dd4124" if x == i else "#7fcdcd" for x in range(len(data))])
            time.sleep(speed)
        for i in range(1, 10):
            count[i] += count[i - 1]
            drawdata(data, ["#dd4124" if x == i else "#7fcdcd" for x in range(len(data))])
        i = n - 1
        while i >= 0:
            index = data[i] // exp
            output[count[index % 10] - 1] = data[i]
            count[index % 10] -= 1
            i -= 1
        i = 0
        for i in range(0, len(data)):
            data[i] = output[i]
            drawdata(data, ["#dd4124" if x == i else "#7fcdcd" for x in range(len(data))])
            time.sleep(speed)
        drawdata(data, ["#dd4124" if x == i else "#7fcdcd" for x in range(len(data))])
        time.sleep(speed)
        exp *= 10
        if c == 3:
            break
    end_time = time.time()
    end_time = int(end_time - start_time)
    color = ["#7fcdcd" for _ in range(len(data))]
    for i in range(len(data)):
        time.sleep(0.01)
        color.insert(i, "#32de84")
        drawdata(data, color)
    return end_time


# shell sort
def ShellSort(data, drawdata, speed):
    start_time = time.time()
    gap = len(data) // 2
    while gap > 0:
        i = 0
        j = gap
        while j < len(data):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                drawdata(data, ["#dd4124" if x == i or x == j else "#7fcdcd" for x in range(len(data))])
                time.sleep(speed)
            i += 1
            j += 1
            k = i
            while k - gap > -1:
                if data[k - gap] > data[k]:
                    data[k - gap], data[k] = data[k], data[k - gap]
                    drawdata(data, ["#dd4124" if x == k or x == k - gap else "#7fcdcd" for x in range(len(data))])
                    time.sleep(speed)
                k -= 1
        time.sleep(speed)
        gap //= 2
    end_time = time.time()
    end_time = int(end_time - start_time)
    color = ["#7fcdcd" for _ in range(len(data))]
    for i in range(len(data)):
        time.sleep(0.01)
        color.insert(i, "#32de84")
        drawdata(data, color)
    return end_time


# selection sort
def SelectionSort(data, drawdata, speed):
    start_time = time.time()
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
                drawdata(data, ["#dd4124" if x == j or x == min_idx else "#7fcdcd" for x in range(len(data))])
                time.sleep(speed)
        data[i], data[min_idx] = data[min_idx], data[i]
    end_time = time.time()
    end_time = int(end_time - start_time)
    color = ["#7fcdcd" for _ in range(len(data))]
    for i in range(len(data)):
        time.sleep(0.01)
        color.insert(i, "#32de84")
        drawdata(data, color)
    return end_time


# heap sort
def HeapSort(data, drawdata, speed):
    start_time = time.time()

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[largest] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            drawdata(data, ["#dd4124" if x == i or x == largest else "#7fcdcd" for x in range(len(data))])
            time.sleep(speed)
            heapify(arr, n, largest)

    def heap_sort():
        n = len(data)
        for i in range(n // 2 - 1, -1, -1):
            heapify(data, n, i)
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, i, 0)

    heap_sort()
    end_time = time.time()
    end_time = int(end_time - start_time)
    color = ["#7fcdcd" for _ in range(len(data))]
    for i in range(len(data)):
        time.sleep(0.01)
        color.insert(i, "#32de84")
        drawdata(data, color)
    return end_time


# merge sort
def MergeSort(data, drawdata, speed):
    start_time = time.time()
    data_local = data
    drawdata_local = drawdata
    speed_local = speed

    def merge_sort(data, drawData, speed):
        merge_sort_alg(data, 0, len(data) - 1, drawData, speed)

    def merge_sort_alg(data, left, right, drawData, speed):
        if left < right:
            middle = (left + right) // 2
            merge_sort_alg(data, left, middle, drawData, speed)
            merge_sort_alg(data, middle + 1, right, drawData, speed)
            merge(data, left, middle, right, drawData, speed)

    def merge(data, left, middle, right, drawData, speed):
        drawData(data, getColorArray(len(data), left, middle, right))
        time.sleep(speed)
        leftPart = data[left:middle + 1]
        rightPart = data[middle + 1: right + 1]
        leftIdx = rightIdx = 0
        for dataIdx in range(left, right + 1):
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                if leftPart[leftIdx] <= rightPart[rightIdx]:
                    data[dataIdx] = leftPart[leftIdx]
                    leftIdx += 1
                    drawData(data, ["#32de84" if left <= x <= right else "#7fcdcd" for x in range(len(data))])
                    time.sleep(speed)
                else:
                    data[dataIdx] = rightPart[rightIdx]
                    rightIdx += 1
                    drawData(data, ["#32de84" if left <= x <= right else "#7fcdcd" for x in range(len(data))])
                    time.sleep(speed)

            elif leftIdx < len(leftPart):
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        drawData(data, ["#dd4124" if left <= x <= right else "#7fcdcd" for x in range(len(data))])
        time.sleep(speed)

    def getColorArray(leght, left, middle, right):
        colorArray = []
        for i in range(leght):
            if left <= i <= right:
                if left <= i <= middle:
                    colorArray.append("#dd4124")
                else:
                    colorArray.append("#dd4121")
            else:
                colorArray.append("#7fcdcd")
        return colorArray

    merge_sort(data_local, drawdata_local, speed_local)
    end_time = time.time()
    end_time = int(end_time - start_time)
    color = ["#7fcdcd" for _ in range(len(data))]
    for i in range(len(data)):
        time.sleep(0.01)
        color.insert(i, "#32de84")
        drawdata(data, color)
    return end_time


# quick sort
def QuickSort(data, head, tail, drawdata, speed):
    start_time = time.time()
    data_local = data
    head_local = head
    tail_local = tail

    def partition(arr, l, h):
        i = (l - 1)
        x = arr[h]
        for j in range(l, h):
            if arr[j] <= x:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                drawdata(data, ["#dd4124" if x == i or x == j else "#7fcdcd" for x in range(len(data))])
                time.sleep(speed)
        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1

    # Function to do Quick sort
    # arr[] --> Array to be sorted,
    # l  --> Starting index,
    # h  --> Ending index
    def quickSortIterative(arr, l, h):
        # Create an auxiliary stack
        size = h - l + 1
        stack = [0] * (size)
        # initialize top of stack
        top = -1
        # push initial values of l and h to stack
        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = h
        # Keep poping from stack while is not empty
        while top >= 0:
            # Pop h and l
            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1
            # Set pivot element at its correct position in
            # sorted array
            p = partition(arr, l, h)
            # If there are elements on left side of pivot,
            # then push left side to stack
            if p - 1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1
            # If there are elements on right side of pivot,
            # then push right side to stack
            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h

    quickSortIterative(data_local, head_local, tail_local)
    end_time = time.time()
    end_time = int(end_time - start_time)
    color = ["#7fcdcd" for _ in range(len(data))]
    for i in range(len(data)):
        time.sleep(0.01)
        color.insert(i, "#32de84")
        drawdata(data, color)
    return end_time

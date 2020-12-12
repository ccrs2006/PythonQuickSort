#This program will generate 1000 random numbers and then sort them 
#using the quick sort method

#import random python library to help generate random numbers
import random

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

#This function will do the quick sort 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
#available option within the random function
#print(dir(random))
numbers = list(range(1,1001))

def randomNumberGen():
  random.shuffle(numbers)

#we shuffle the numbers list of number to get random numbers
#and store it in a new variable named arr
randomNumberGen()
#we generate a new variable that contains the new shuffled numbers
randomNumbers = numbers

#Driver code
arr = randomNumbers
print("original arrary is:")
print(randomNumbers)  
n = len(arr)
quickSort(arr, 0, n-1)
print("New quick sorted array is:")
for i in range(n):
    print(arr[i], end = ", ")

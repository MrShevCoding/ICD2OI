# Bozosort

Sorting algorithms are procedures for sorting lists of items. Many different sorting algorithms exist, each with their own pros, cons and use cases. One of the worst ones, Bozosort, works the following way: 

***While the list is not in order, pick two items at random and swap them, then check to see if the list is sorted.***

Your task: implement Bozosort in Python.

Create the function bozoSort() that takes in a list of integers, and returns the sorted version of the list. The function should also return the number of swaps it had to make in order to sort the list.

**Use the following code to test your function:** 

unsorted \= \[8,2,44,6,24,9,10,16,5\]

results \= bozoSort(unsorted)

print("The sorted list is", results\[0\], "and it took", results\[1\], "swaps to sort")

def quickSort(theList):
    quickSortHelper(aList, 0, len(theList)

def quickSortHelper(theList, start, end):
    if start <= end:                            # If there are two or more elements...
        split = partition(theList, start, end)    # ... partition the sublist...
    else:
        return

def partition(theList, start, end):
    pivot = theList[end]                       # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0
    while not done:                            # Until we find an out of place element...
        top = top-1                            # ... move the top down.

        if top == bottom:                      # If we hit the bottom...
            done = 1                           # ... we are done.
            break

        if theList[top] < pivot:               # Is the top out of place?
            theList[bottom] = theList[top]     # Then put it at the bottom...
            break                              # ...and start searching from the bottom.


    theList[top] = pivot                       # Put the pivot in its place.
    return top                                 # Return the split point


def main():
    myList = [3, 2, 33, 1, 9, 90, 0, 5, 31, 12]
    quickSort(myList)
    print(myList)

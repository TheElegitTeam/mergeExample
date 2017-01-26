def quickSort(theList):
    quickSortHelper(aList, 0, len(theList)

def quickSortHelper(theList, start, end):
    if start <= end:                            # If there are two or more elements...
        split = partition(theList, start, end)    # ... partition the sublist...
    else:
        return

def partition(theList, start, end):
    pivot = theList[end]                       # Partition around the last value
def quickSort(aList):
    if start < end:                             # If there are two or more elements...
        split = partition(aList, start, end)    # ... partition the sublist...
        quicksort(aList, start, split-1)        # ... and sort both halves.
        quicksort(aList, split+1, end)
    else:
        return

def quickSortHelper(aList, start, end):

def partition(aList, start, end):
    pivot = aList[end]                         # Partition around the last value
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
    while not done:                            # Until all elements are partitioned...

      while not done:                          # Until we find an out of place element...
          bottom = bottom+1                    # ... move the bottom up.

          if bottom == top:                    # If we hit the top...
              done = 1                         # ... we are done.
              break

          if aList[bottom] > pivot:            # Is the bottom out of place?
              aList[top] = aList[bottom]       # Then put it at the top...
              break                            # ... and start searching from the top.

    aList[top] = pivot                         # Put the pivot in its place.
    return top                                 # Return the split point


def main():
    myList = [3, 2, 33, 1, 9, 90, 0, 5, 31, 12]
    myList = [3, 2, 23, 1, 9, 0, 0, 3, 45, 2]
    quickSort(myList)
    print(myList)

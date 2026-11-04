#HW1.1
def selection_sort(array):
    n = len(array)
    for i in range(n-1): #last element will be in correct location automatically
        smallest = array[i]
        smallest_ind = i
        for j in range(i+1,n): 
            if array[j]<smallest:
               smallest = array[j]
               smallest_ind = j
        #swap if necessary
        if smallest_ind != i:
           (array[i], array[smallest_ind]) = (array[smallest_ind], array[i])
#arr=[-4,11,7,-12,6,1]
#(selection_sort(arr))
#print(arr)
#1.2
def bubble_sort(array):
    ordered = False
    n = len(array)
    while not ordered:
        ordered = True 
        for i in range(n-1):
            if array[i]> array[i+1]:
                (array[i],array[i+1]) = (array[i+1], array[i])
                ordered = False

#array = [-4,11,7,-12,6,1]
#bubble_sort(array)
#print(array)


#2
def selection_sort(array):
    n = len(array)
    for i in range(n-1): #last element will be in correct location automatically
        smallest = array[i]
        smallest_ind = i
        for j in range(i+1,n): 
            if array[j]<smallest:
               smallest = array[j]
               smallest_ind = j
        #swap if necessary
        if smallest_ind != i:
           print(array)
           (array[i], array[smallest_ind]) = (array[smallest_ind], array[i])
#arr=[-4,11,7,-12,6,1]
#(selection_sort(arr))
#print(arr)

def bubble_sort(array):
    ordered = False
    n = len(array)
    while not ordered:
        ordered = True 
        for i in range(n-1):
            if array[i]> array[i+1]:
                print(array)
                (array[i],array[i+1]) = (array[i+1], array[i])
                ordered = False
#array = [-4,11,7,-12,6,1]
#bubble_sort(array)
#print(array)

#HW3
def insertion_sort(array):
    i = 1
    n = len(array)
    while i < n:
        val = array[i]
        j = i-1
        while j >= 0 and array[j]> val:
            array[j+1] = array[j]
            j = j-1
        array[j+1]=val
        i += 1
    else:
        return array

array = [9,7,2,11]
insertion_sort(array)
print(array)





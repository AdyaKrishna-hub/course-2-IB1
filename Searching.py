#sequential search
#def seq_search(key,array):
#    index = 0
#    found = False
#    while not found and index < len(array):
#        if array[index] == key:
#            found = True
#        index += 1
#    return found
#arr = [7,-22,4,56,8]
#print(seq_search(4,arr))
#print(seq_search(57,arr))

#def time_search(algo,n,/,sort_data=False):
#    import random, time
#    data = random.choices(range(n), k = n)
#    if sort_data:
#        data.sort()
 #   key = n

 #   start = time.process_time()
 #   algo(key,data)
#    end = time.process_time()
#    return end-start
#print(time_search(seq_search,10**4))



#Parallel arrays
#key = 'Mary'
#names = ['John', 'Mary', 'Diana']
#rooms = [111,123,111]
#index = 0
#found = False
#while not found and index < len(names):
#    if names[index] == key:
#        found = True
#    else:
#        index += 1
#if found:
#    print(rooms[index])
#else:
#    print(f'{key} not a guest here')


#class Reservations:
#    def __init__(self,name,room):
#        self.name = name
#        self.room = room
#reservations = [Reservations('John', 111), Reservations('Mary',123), Reservations('Diana',111)]
#index = 0
#found = False
#key = 'Dave'
#while not found and index < len(reservations):
#    if reservations[index] == key:
#        found = True
#    else:
#        index += 1
#if found:
#    print(reservations[index].room)
#else:
#    print(f'{key} not a guest here')


#HW2
#key = 'Charlie'
#students = ['Alissa', 'Ben', 'Charlie', 'Dianna']
#grades = ['B','D','B','A']
#index = 0
#found = False
#while not found and index <len(students):
#    if students[index]==key:
#        found = True
#    else:
#        index += 1
#if found:
#    print(grades[index])

#binary search
def bin_search(key,array):
    lo = 0
    hi = len(array)-1
    while lo <= hi:
        mid = (lo+hi) // 2
        val = array[mid]
        print(val)
        if key == val:
            print(val)
            return True
        elif key< val:
            hi = mid -1
        else: #key > val
            lo = mid + 1
    return 'found'

lst = [-2,3,6,11,223,1001]
print(bin_search(3,lst))  
#print(bin_search(10,lst))  



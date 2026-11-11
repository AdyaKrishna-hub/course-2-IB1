def seq_search(key,array):
    index = 0
    found = False
    while not found and index < len(array):
        if array[index] == key:
            found = True
        index += 1
    return found
arr = [7,-22,4,56,8]
print(seq_search(4,arr))
print(seq_search(57,arr))
print(seq_search('hi',arr))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

#import pickle, pathlib # pickle for storage, hehe
#file_path = pathlib.Path('data') / 'points.ser' # file on drive
#points_written = [Point(x, x**2) for x in range(20)] # some data
#print(points_written[-1]) # last point written

# serialize / pickle onto drive
#f = open(file_path, 'wb') # open file for writing binary data
#pickle.dump(points_written, f) # save data into file
#f.close() # close file

# deserialize / unpickle from drive
#f = open(file_path, 'rb') # open for reading binary data
#points_read = pickle.load(f) # read and return data
#f.close() # close file
#print(points_read[-1]) # last point read

#EX4
#try:
#    import pathlib
#    file_path = pathlib.Path('data') / 'points.txt'
#    with open(file_path) as f:
#        points_read = []
#        for line in f: # traverse lines
            # extract x, y
#            [x, y] = [int(word) for word in line.split()]
#            points_read.append(Point(x, y))
#    print(points_read[-1])
#except Exception as e: # handle any exception raised
#    print('exception:', e)

#EX5
#completed = False
#while not completed:
#    try:
#        filename = input('give file name: ')
#        with open(filename, 'at') as f:
#            print(440,file=f)
#        completed = True #if an exception is raised, this will never be executed
#    except Exception as e:
#        print('nope, try again')


#HW1
#1.1
import random
b = [random.randint(1, 100) for _ in range(10)]

#HW1.2

#HW2
#print(float('yay'))

#while True:
#    y = input('give a decimal number: ')
#    try:
#        y = float(y)
#        print('bye bye')
#        break
#    except Exception as e:
#        print('exception:', e)

#HW3
h = input('give a file name: ')
sum = 0
num = 0
try:
    with open(h) as f:
        for line in f:
            numbers = line.split()
            for n in numbers:
                sum += float(n)
                num +=1
    if num > 0:
        print(sum / num)
    else:
        print("The file was empty!")
except Exception as e:
    print('exception:',e)





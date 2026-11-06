#EX4
class Product:
    def __init__(self, model, price): # adding a new class
            self.model = model
            self.price = price
    def __str__(self):
        return self.model + '@' + str(self.price)
class Laptop(Product): #shows inheritance
    def __init__(self, model, price):
        super().__init__(model,price)

class Router:
    def __init__(self, model, price):
        super().__init__(model,price)

class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product): 
        self.product.append(product)
    def __str__(self):
        return ' '.join([str(p) for p in self.products])

class Warehouse: #maybe you want to keep the laptops and routers separate in the warehouse
    def __init__(self, laptops, routers):
        self.laptops = laptops
        self.routers = routers

warehouse = Warehouse([Laptop('mac', 1999)], [Router('netgate', 600)])
order = Order()
order.add_product(warehouse.laptops[0])
order.add_product(warehouse.router[0])
print(order)




#HW1
class Book:

    def __init__(self,title,authors,publication_year):
        self.title= title
        self.authors = authors
        lst =[]
        lst.append(self.authors)
        self.publication_year = publication_year
    def __str__(self):
        auth = ' & '.join(self.authors)
        return f'{auth}: {self.title}({self.publication_year})' 
    def num_authors(self):
        return len(self.authors)
clrs = Book('Introduction to Algorithma(3rd ed.)', ['Cormen','Leiserson','Rivest','Stein'], 2009)
print(clrs)

#1.2
books = [Book('Introduction to Algorithma(3rd ed.)', ['Cormen','Leiserson','Rivest','Stein'], 2009), 
         Book('book', ['somebody', 'somebody else'], 2015),
         Book('another book', ['Jarmo'], 2000)] 
for b in books:
    print(b)
#1.3
books.sort(key=lambda b: b.num_authors(), reverse = True)
for b in books:
    print(b)

#HW2
class Newspaper:
    def __init__(self, name, year, month, day_of_month,is_finnish):
        self.__name= name
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.is_finnish=is_finnish
    def get_name(self):
        return self.__name
    def __str__(self):
        return f'{self.__name},{self.year},{self.month},{self.day_of_month},{self.is_finnish}'
paper = Newspaper('Helsingin Sanomat', 2025,9,19,True)
print(paper)
print(paper.get_name())

#HW3
class Course:
    def __init__(self,name,topic,name_of_teacher,num_participants):
        self.name = name
        self.topic = topic
        self.name_of_teacher= name_of_teacher
        self.num_participants= num_participants
    def __str__(self):
        return f'{self.name}, {self.topic}, {self.name_of_teacher}, {self.num_participants}'
course = Course('CS SL','Coding', 'Jarmo','100000')
print(course)
print(course.__str__())


#HW4
import math
class Point:
    def __init__(self,x,y):
        self.x= x
        self.y=y
    def is_on_x_axis(self):
        is_it= False
        if self.y == 0:
            is_it = True
        return is_it
    def same_as_another_point(self,other):
        b = False
        if self.x == other.x and self.y == other.y:
            b = True
        return b
    def distance(self,other):
        g = math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)
        return g
    def in_unitcircle(self):
        if self.x**2+self.y**2 <= 1:
            return True
        else:
            return False
    def midpoint(self,other):
        j = (self.x+other.x)/2
        h = (self.y+other.y)/2
        return (j,h)

a = Point(3,0)
b = Point(0,4)
print(a.is_on_x_axis())
print(b.is_on_x_axis())
print(a.distance(b))
print(Point(1,1).in_unitcircle())
print(a.midpoint(b))



    
    



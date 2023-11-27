import math
pi = math.pi

"""Define classes for circle and right triangle. Set method to calculate
area in each class. Also, define error when input is 0 or negative."""
class Circle():
    def __init__(self,r):
        if r <= 0:
            raise ValueError("Input smaller or equal to 0. Try again.\n")
        self.radius  = r
        
    def area(self):
        return (self.radius**2) * pi
    
class Right_triangle():
    def __init__(self,s):
        if s <= 0:
            raise ValueError("Input smaller or equal to 0. Try again.\n")
        self.side = s
        
    def area(self):
        return (math.sqrt(3)/4) * (self.side**2)

def find_the_area_of_intersection():
    r = float(input("Input the radius: "))
    #Area = (two 1/6 circle area - 1 right triangle area) * 2
    area_of_intersection = (((1/6) * Circle(r).area() *2) - Right_triangle(r).area())*2
    #Round the result to second decimal place
    print(round(area_of_intersection, 2))
    return
    
if __name__ == "__main__":
    while True:
        
        try:
            find_the_area_of_intersection()
            break
        
        except ValueError as msg:
            print(msg)
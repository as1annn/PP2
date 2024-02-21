class Shape :
    def __init__ (self,length = 0 ):
        self.lenthg = length
        def area(self):
            return ( 3,14 * self.length * self.length)
        class Square(Shape):
           def __init__ (self, length=0):
              super().__init__(length)
        def volume(self):
            return (4/3 * 3,14 * self.length * self.length *self.length)
        shape = Shape(5)
        print("shape:", shape.volume())
        square = Square(4)
        print("square:", square.area())
    



        
            

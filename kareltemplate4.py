"""==========KAREL TEMPLATE=========="""
class ktools:
    def m(self):
        # Shorthand for move
        move()
        
    def tl(self):
        # Turn Left
        turn_left()
    
    def tr(self):
        # Turn Right
        self.tl()
        self.tl()
        self.tl()
    
    def ta(self):
        # Turn Around
        self.tl()
        self.tl()
    
    def pick(self):
        # Pick Beeper
        take_ball()
    
    def put(self):
        # Put Beeper
        put_ball()
    
    def put2(self):
        # Put 2 beepers in a line
        self.put()
        self.m()
        self.put()
    
    def put5(self):
        # Put 5 beepers in a line
        self.put2()
        self.m()
        self.put2()
        self.m()
        self.put()
    
    def h(self):
        # Print H using beepers
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.tr()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()
    
    def e(self):
        pass
    
    def l(self):
        pass
    
    def o(self):
        pass
    
    def fic(self):
        # Front is Clear (True or False)
        return front_is_clear()
        
    def fib(self):
        # Front is Blocked
        return not self.fic()
        
    def ric(self):
        # Right is Clear
        self.tr()
        if self.fic():
            self.tl()
            return True  # Immediately exit the function
        self.tl()
        return False
        
    def rib(self):
        # Right is Blocked
        return not self.ric()
        
    def mazemove(self):
        # Maze Move
        if self.fib():
            self.tl()
        else:  # Otherwise...
            self.m()
            if self.ric():
                self.tr()
                self.m()
                if self.ric():
                    self.tr()
                    self.m()
        pass
    
    
    def mm(self, repeats):
        # Move Multiple
        for number in range(0, repeats):
            self.m()
            
    def putm(self, repeats):
        # Put Multiple
        for num in range(repeats - 1):
            self.put()
            self.m()
        self.put()
        
    def pickm(self, repeats):
        # Pick Multiple
        for num in range(repeats - 1):
            self.pick()
            self.m()
        self.pick()
        
    def one(self):
        self.tl()
        self.putm(5)
        self.ta()
        self.mm(4)
        self.tl()
        self.mm(2)
        
    def zero(self):
        pass
    
    def SOB(self):
        # Standing on Beeper
        return balls_present()
        
    def jump(self):
        # Jump for 510
        while self.fic():
            self.m()
        self.tl()
        while self.rib():
            self.m()
        self.tr()
        self.m()
        self.tr()
        while self.fic():
            self.m()
        self.tl()
    
    def find(self):
        # Find for 515
        while not facing_north():
            self.tl()
        self.m()
        if not self.SOB():
            self.tl()
            self.m()
            self.tl()
            self.m()
        for num in range(2):
            if not self.SOB():
                self.m()
                self.tl()
                self.m()
        pass
        

kt = ktools()
"""==========KAREL CODE HERE=========="""
# while kt.SOB():
#     kt.pick()
#     kt.find()


pass

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
    

kt = ktools()
"""==========KAREL CODE HERE=========="""
# kt.h()
# kt.e()

pass

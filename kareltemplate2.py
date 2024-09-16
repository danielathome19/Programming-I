"""========== KAREL LIBRARY =========="""
def m():
    # Shorthand for 'move()'
    move()
    
def tl():
    # Turn Left
    turn_left()
    
def tr():
    # Turn Right
    tl()
    tl()
    tl()

def ta():
    # Turn Around
    tl()
    tl()

def pick():
    # Pick Beeper
    take_ball()
    
def put():
    # Put Beeper
    put_ball()
    
def put2():
    # Put 2 beepers in a line
    put()
    m()
    put()

def put5():
    # Put 5 beepers in a line
    put2()
    m()
    put2()
    m()
    put()

def H():
    # Print H using beepers
    tl()
    put5()
    ta()
    m()
    m()
    tl()
    m()
    put2()
    m()
    tl()
    m()
    m()
    ta()
    put5()
    tl()
    m()
    m()
    
def E():
    pass

def L():
    pass

def O():
    pass

def fic():
    # Front is Clear (True or False)
    return front_is_clear()

def fib():
    # Front is Blocked
    return not fic()

def ric():
    # Right is Clear
    tr()
    if fic():
        tl()
        return True  # Immediately exit the function
    tl()
    return False

def rib():
    # Right is Blocked
    return not ric()
    
def mazemove():
    # Maze Move
    if fib():
        tl()
    else:  # Otherwise...
        m()
        if ric():
            tr()
            m()
            if ric():
                tr()
                m()
    pass

"""========== END KAREL LIBRARY =========="""

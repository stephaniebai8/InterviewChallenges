"""
Please refactor this code to make it more readable and more robust
Furthermore, add some tests to check edge cases in the tests directory.
Name the test file 'testee_added_general.py'
"""


def f(x):
    return x * x 


def g(f):
    return lambda x: f(f(x)) 
    

def h(x):
    return x[0]
    
    
def j(l):
    return l[-1] 

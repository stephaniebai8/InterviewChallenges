"""
Please refactor this code to make it more readable and more robust
Furthermore, add some tests to check edge cases in the tests directory.
Name the test file 'testee_added_general.py'
"""


def square(x: int) -> int:
    return x * x 


def cube(f: int) -> int:
    cubed = lambda f: square(f) * f
    return cubed(f)
    

def firstLetter(x:str) -> chr:
    return x[0]
    
    
def lastLetter(l:str) -> chr:
    return l[-1]
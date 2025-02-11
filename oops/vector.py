""" 
define a vector class which can add or substract 2 vectors 
generally 3 dimensional vector i , j, k 

eg. v_a = <5,-2,3>
    v_b = <1,4,3>
    v_result = <6,2,5>
"""

class Vector:
    def __init__(self,j,k,l):
        self._j = j
        self._k = k
        self._l = l

    def add(self,v_a,v_b):
        


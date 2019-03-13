# In the multiple inheritance scenario, any specified attribute is searched first in the current class.
# If not found, the search continues into parent classes in depth-first,
# left-right fashion without searching same class twice.

# This order is also called linearization of MultiDerived class and the set of
# rules used to find this order is called Method Resolution Order (MRO).

class Base1:
    pass

class Base2:
    pass

class Derived(Base1,Base2):
    pass

# print (Derived.__mro__)


class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass
class N(A,B,Z): pass

print(M.mro())
print(N.mro())
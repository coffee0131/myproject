#Ex-8. Set class에 methods 추가와 git 활용 (4/23)
#OOP 3 강의노트에 적힌 대로 method 및 operator를 추가하고 시험하라.

#vscode와 git을 활용하여 개발하고, GitHub의 repository URL link를 eclass에 적으면 충분하다.
class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)
#Test whether the set is a proper subset of other, 
# that is, set <= other and set != other.
    def issubset(self, other):
        if list(self) == list(other):
            return False
        for x in self.data:               
            if not x in other:
                return False
        return True

    def issuperset(self, other):
        for x in other.data:               
            if not x in self:
                return False
        return True

#Update the set, keeping only elements found in it and all others.
    def intersection_update(self,other):
        res = self.data[:]            
        for x in other:               
            if not x in res:
                res.append(x)
        self.data = []
        self.data = res
        return self
#Update the set, removing elements found in others.

    def difference_update(self,other):
        res = self.data[:]
        res2 = self.intersection(other)    
        self.data = []
        for x in res:
            if not x in res2:
                self.data.append(x)
        return self
#Update the set, keeping only elements found in either set, but not in both.

    def symmetric_difference_update(self,other):
        res = self.intersection(other)
        res2 = self.union(other)       
        self.data = []
        for x in res2:
            if not x in res:
                self.data.append(x)
        return self

#Add element elem to the set.

    def add(self, elem):
        self.data.append(elem)
        print("add completely\n")
        return self

#self.remover(elem)
    def remover(self, elem):
        res = []
        # raise keyerror finder
        try:
            self.data.remove(elem)
        except KeyError as elem:
            print("KeyError: ",elem)
        for x in self.data:
            if x != elem:             # remove elem
                res.append(x)
        self = []
        self = res
        print("remover completely\n")
        return self

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
 
    



x = Set([1,3,5,7])
y = Set([3,5,1])
z = Set([1,3,5,7])
w = Set([2,4])

print(x)
print(y)
print(z)
print(w)

print("issubset test")
print(x,"is subset of",y,"?: ",x.issubset(y)) 
print(y,"is subset of",x,"?: ",y.issubset(x)) 
print(z,"is subset of",x,"?: ",z.issubset(x)) 
print(x,"is subset of",z,"?: ",x.issubset(z))
print(x,"is subset of",w,"?: ",x.issubset(w)) 
print("\n")

print("issuperset test")
print(x,"is superset of",y,"?: ",x.issuperset(y)) 
print(y,"is superset of",x,"?: ",y.issuperset(x)) 
print(z,"is superset of",x,"?: ",z.issuperset(x)) 
print(x,"is superset of",z,"?: ",x.issuperset(z)) 
print(x,"is superset of",w,"?: ",x.issuperset(w)) 
print("\n")

print("intersection_update test")
print("x is",x) 
print("intersection_update(x,y)",x.intersection_update(y))
print("modified x is",x) 
print("y is",y)
print("intersection_update(y,x)",y.intersection_update(x))
print("modified y is",y)
print("w is",w)
print("intersection_update(w,x)",w.intersection_update(x))
print("modified w is",w) 
print("\n")

print("difference_update test")
print("x is",x)
print("difference_update(x,y))",x.intersection_update(y))
print("modified x is",x) 

print("symmetric_difference_update test")
print("x is",x)
print("symmetric_difference_update(x,y)",x.symmetric_difference_update(y))
print("modified x is",x)
print("w is",w)
print("symmetric_difference_update(w,z)",w.symmetric_difference_update(z))
print("modified w is",w)
print("\n")


#def add(self, elem):
#def remover(self, elem):

print("add test")
print("x",x,"add 3 to x =",x.add(3))
print("\n")

print("remover all 3 test")
print("x",x,"remove all 3 to x =",x.remover(3))
print("\n")

# raise keyerror
#print("remover all 4 test")
#print("x",x,"remove all 4 to x =",x.remover(4))
#print("\n")



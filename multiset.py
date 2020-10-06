#author -- orsessential
class Multiset(object):
    m = []       
    def add(self, val):
        return self.m.append(val)
        
    def remove(self, val):
        if val in self.m:
            return self.m.remove(val)
        else:
            return False
    def _contains_(self, val):
        if val in self.m:
            return True
        else:
            return False
    
    def _len_(self):
        return len(self.m)

    
def Operations(operation):
    m = Multiset()
    result = []
    for opt in operation:
        el = opt.split()
        if el[0] == 'size':
            result.append(len(m))
        else:
            op, val = el[0], int(el[1])
            if op == 'query':
                result.append(val in result)
            elif op == 'add':
                m.add(val)
                print(m)
            elif op == 'remove':
                m.remove(val)
                print(m)
    return result

i = int(input())
operationss = []
for _ in range (i):
    operationss.append(input())
result = Operations(operationss)
print(result)




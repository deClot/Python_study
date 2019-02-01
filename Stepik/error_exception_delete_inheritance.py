def is_ancestry(child, parent):
    

'''
def find_parent(parent, child):
    if parent == child:
        return True
    if len(parents[child]) == 0:
            return False
        
    for i in range(len(parents[child])):
        if parents[child][i] == parent:
            return True
        else:
            if find_parent(parent, parents[child][i]) is True:
                return True
            else:
                continue
    return False
'''

n = input() # number of exceptions
exceptions = {}

for _ in range(int(n)):
    string = input().split()

    if len(string) > 1:
        exceptions[string[0]] = string[2:]

    else:
        exceptions[string[0]] = []

m = input() # number of inputed exceptions
input_exceptions = []
out = []

for _ in range(int(m)):
    exception = input()
    input_exceptions.append(exception)

    for i in range(len(input_exceptions)-1):
        flag = is_ancestry(exception, input_exceptions[i])

        if flag == False:
            continue
        else:
            print (exception)
            break
    
    

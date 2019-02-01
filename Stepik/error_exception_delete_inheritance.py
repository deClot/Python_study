def find_ancestry(excesption, parents, input_exception):
    if len(parents) == 0:
        return False
    
    if input_exception in parents:
        return True
    else:
        for parent in parents:
            find_ancestry(parent, exceptions[parent], input_exception)
    

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
    parents = exceptions[exception]

    for i in range(len(input_exceptions)-1):
        flag = find_ancestry(exception, parents, input_exceptions[i])

        if flag == False:
            continue
        else:
            print (exception)
            break
    
    

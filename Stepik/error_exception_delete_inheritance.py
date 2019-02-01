def is_ancestry(child, parent):
    return child == parent or any(map(lambda p: is_ancestry(p, parent), exceptions[child]))
    
n = input() # number of exceptions
exceptions = {}

for _ in range(int(n)):
    string = input().split()
    exceptions[string[0]] = [] if len(string) == 1 else string[2:]

m = input() # number of inputed exceptions
input_exceptions = []
out = []

for _ in range(int(m)):
    child = input()
    input_exceptions.append(child)

    for i in range(len(input_exceptions)-1):
        parent = input_exceptions[i]
        flag = is_ancestry(child, parent)

        if flag == False:
            continue
        else:
            print(child)
            break
    
   

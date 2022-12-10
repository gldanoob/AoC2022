import sys


with open('../' + sys.argv[1]) as f:

    arr = [[] for i in range(9)]
    lines = f.read().splitlines()

    init = True

    for line in lines:
        if not len(line): 
            init = False
            arr = [a[::-1] for a in arr]

            continue
        if init:
            for i in range(9):
                c = line[i*4+1]
                if c != ' ' and not c.isdigit(): arr[i].append(c)
        else:
            line = line.replace('move ', '').replace('from ', '').replace('to ', '')
            a, b, c = (int(i) for i in line.split())
            arr[c-1].extend(arr[b-1][-a:])
            for i in range(a): arr[b-1].pop()
    print(''.join(a[-1] for a in arr if len(a)))


        
    


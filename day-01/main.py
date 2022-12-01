import sys

with open('../' + sys.argv[1]) as f:
    arr = [0] 
    for line in f.read().splitlines():
        if not line: arr.append(0)
        else: arr[-1] += int(line)
        
    print(max(arr)) 
    print(sum(sorted(arr)[-3:]))
   
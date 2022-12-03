import sys

with open('../' + sys.argv[1]) as f:
    s = 0
    lines = f.read().splitlines()
    for line in lines:
        n = len(line)
        i = set(line[:n//2]).intersection(set(line[n//2:]))
        c = i.pop()
        s += ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27
    print(s)

    s = 0
    for i in range(0, len(lines), 3):
        i = set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2]))
        c = i.pop()
        s += ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27

    print(s)

import sys

with open('../' + sys.argv[1]) as f:
    data = f.read()
    lines = data.splitlines()
    count = 0
    count2 = 0
    for line in lines:
        x, y = line.split(',')
        a, b = (int(i) for i in x.split('-'))

        c, d = (int(i) for i in y.split('-'))

        if a <= b and c >= d or a >= b and c <= d:
            count += 1

        q = set(range(a, b+1))
        w = set(range(c, d+1))
        if len(q & w):
            count2 += 1

    print(count)

    print(count2)

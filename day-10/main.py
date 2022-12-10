import sys

with open('../' + sys.argv[1]) as f:
    lines = f.read().splitlines()

    p = []
    for line in lines:
        i = line
        a = 0
        if ' ' in line:
            i, a = line.split()
            a = int(a)
        p.append((i, a))

    w = False
    x = 1
    cy = 0
    c = 0
    s = 0
    px = [' '] * 40
    while c < len(p):
        cy += 1
        if cy in (20, 60, 100, 140, 180, 220):
            s += cy * x
        if abs(x + 1 - (cy % 40)) <= 1:
            px[(cy - 1) % 40] = '#'
        match p[c][0]:
            case 'noop': c += 1
            case 'addx':
                w = not w
                if not w:
                    x += p[c][1]
                    c += 1
        if cy % 40 == 0:
            print(''.join(px))
            px = [' '] * 40
print(s)

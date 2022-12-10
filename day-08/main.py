import sys

with open('../' + sys.argv[1]) as f:
    arr: list[list[int]] = []
    scores = []
    lines = f.read().splitlines()
    for line in lines:
        arr.append([int(i) for i in line])

    c = 0

    for y, row in enumerate(arr):
        for x, t in enumerate(row):
            l, r, u, b = x, len(row) - x - 1, y, len(arr) - y - 1
            if 0 in (x, y) or x == len(row) - 1 or y == len(arr) - 1:
                c += 1
            elif all(a < t for a in row[:x]) or all(a < t for a in row[x+1:]):
                c += 1
            elif all(r[x] < t for r in arr[:y]) or all(r[x] < t for r in arr[y+1:]):
                c += 1

            for i, v in enumerate(row[:x][::-1]):
                if v >= t:
                    l = i + 1
                    break

            for i, v in enumerate(row[x+1:]):
                if v >= t:
                    r = i + 1
                    break

            for i, v in enumerate([r[x] for r in arr[:y]][::-1]):
                if v >= t:
                    u = i + 1
                    break

            for i, v in enumerate(r[x] for r in arr[y+1:]):
                if v >= t:
                    b = i + 1
                    break

            s = l*r*u*b
            scores.append(s)

    m = scores.index(max(scores))
    print(c)
    print(max(scores))

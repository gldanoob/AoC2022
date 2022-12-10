import sys


def sign(x):
    if not x:
        return 0
    return 1 if x > 0 else -1


with open('../' + sys.argv[1]) as f:
    arr = []
    lines = f.read().splitlines()
    x = [10] * 10
    y = [10] * 10
    for line in lines:
        m, r = line.split()
        r = int(r)

        for i in range(r):
            bruh = [[' '] * 20 for i in range(20)]
            match m:
                case 'R': x[0] += 1
                case 'U': y[0] -= 1
                case 'L': x[0] -= 1
                case 'D': y[0] += 1

            for i in range(9):
                if abs(x[i] - x[i+1]) == 2:
                    x[i+1] += int((x[i] - x[i+1]) / 2)
                    if y[i] != y[i+1]:
                        y[i+1] += sign(y[i] - y[i+1])
                if abs(y[i] - y[i+1]) == 2:
                    y[i+1] += int((y[i] - y[i+1]) / 2)
                    if x[i] != x[i+1]:
                        x[i+1] += sign(x[i] - x[i+1])

            if (x[9], y[9]) not in arr:
                arr.append((x[9], y[9]))

            for b in bruh:
                print(''.join(str(i) for i in b))
            print()

    print(len(arr))

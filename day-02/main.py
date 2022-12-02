import sys



with open('../' + sys.argv[1]) as f:
    score = 0
    another_score = 0
    for line in f.read().splitlines():
        a, b = line.split()
        a = ord(a) - ord('A') + 1
        b = ord(b) - ord('X') + 1

        win = b > a if a * b != 3 else b < a 
        if win: score += 6
        elif a == b: score += 3
        score += b

        match b:
            case 1: another_score += (a - 2) % 3 + 1 
            case 2: another_score += 3 + a
            case 3: another_score += 6 + a % 3 + 1 

    print(score)
    print(another_score)


    
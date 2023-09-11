target = input()

def calc_dist(target):
    target = abs(int(target))
    dist = 0
    nMoves = 0
    while target > dist or (dist - target) % 2 != 0:
            nMoves += 1
            dist += nMoves
    return nMoves

print(calc_dist(target))
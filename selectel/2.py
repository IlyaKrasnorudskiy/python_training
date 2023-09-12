

def calc_dist(target):
    target = abs(int(target))
    dist = 0
    nMoves = 0
    while target > dist or (dist - target) % 2 != 0:
            nMoves += 1
            dist += nMoves
            print("dist: " + str(dist) + ", nMoves: " + str(nMoves))
    return nMoves



for target in range(2, 100):
    print("Target = " + str(target))
    print(calc_dist(target))



def hanoiTower(n, source, dest, temp):
    if (n == 1):
        print("Move a disk from peg %d to peg %d" % (source, dest))


    else:
        hanoiTower(n-1, source, temp, dest)
        print("Move a disk from peg %d to peg %d" % (source, dest))
        hanoiTower(n-1, temp, dest, source)



n = int(input("하노이 입력 : "))

hanoiTower(n, 1, 3, 2)
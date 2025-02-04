def solve(numheads, numlegs):
    rab = (numlegs - 2*numheads)/ 2
    chick = numheads - rab
    print("rabbits: ", rab)
    print("chickens: ", chick)

solve(35, 94)
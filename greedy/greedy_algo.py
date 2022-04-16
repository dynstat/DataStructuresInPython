# output = 18, available coins {5,2,1}

def greedy(output: int, coins: set):
    soln_set = []
    s = 0

    while (True):
        m = max(coins)
        t = s + m
        if t == output:
            s = t
            soln_set.append(m)
            return soln_set
        if t < output:
            s = t
            soln_set.append(m)
        else:
            coins.remove(m)


print(greedy(18, {5, 2, 1}))

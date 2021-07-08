def which_tetrahedral(t):

    # the n'nt number tetrahedral
    nT = 0

    # counting variable
    n = 0

    # if t > nT -> not a tetrahedral number
    while t > nT:

        # Find next tetrahedral
        nT = (n * (n + 1) * (n + 2)) / 6

        # Test if found
        if t == nT:
            return n
        else:
            n += 1

    # If not found return 0
    return 0


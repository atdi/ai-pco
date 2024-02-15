portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0]
]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]


def permutate(arr):
    if len(arr) == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        remaining = arr[:i] + arr[i + 1:]
        for r in permutate(remaining):
            result.append([arr[i]] + r)
    return result


def permutations(route, ports):
    smallest_emissions = 1000000
    local_bestroute = [0, 0, 0, 0, 0]
    all_routes = permutate(ports)
    for r in all_routes:
        full_route = route + r
        emissions = 0
        print(full_route)
        for i in range(len(full_route) - 1):
            emissions += D[full_route[i]][full_route[i + 1]]
        if emissions < smallest_emissions:
            smallest_emissions = emissions
            local_bestroute = full_route
    print(local_bestroute)
    return local_bestroute, smallest_emissions * co2


def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion
    bestroute, smallest = permutations([0], list(range(1, len(portnames))))
    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)


if __name__ == '__main__':
    main()

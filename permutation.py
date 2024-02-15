portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


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
    # Write your recursive code here
    result = permutate(ports)
    for r in result:
        route = route + r
        print(' '.join([portnames[i] for i in route]))
        route = [route[0]]


if __name__ == '__main__':
    permutations([0], list(range(1, len(portnames))))

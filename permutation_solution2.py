portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i] + ports[i + 1:])


if __name__ == '__main__':
    permutations([0], list(range(1, len(portnames))))
import math
import random  # just for generating random mountains

# generate random mountains

w = [.05, random.random() / 3, random.random() / 3]
h = [1. + math.sin(1 + x / .6) * w[0] + math.sin(-.3 + x / 9.) * w[1] + math.sin(-.2 + x / 30.) * w[2] for x in
     range(100)]


def climb(x, h):
    # keep climbing until we've found a summit
    summit = False
    max_rigth = 0
    max_left = 0
    for i in range(x, x+5):
        if max_rigth < h[i]:
            max_rigth = h[i]
    for i in range(x-5, x):
        if max_left < h[i]:
            max_left = h[i]
    go_right = max_rigth > max_left
    # edit here
    while not summit and x >= 0:
        summit = True  # stop unless there's a way up
        next = 0
        if not go_right:
            next = x - 5
            for i in range(next, x):
                if h[i] > h[x]:
                    summit = False
                    x = i
                    break
        else:
            next = x + 5
            for i in range(x, next):
                if h[i] > h[x]:
                    summit = False
                    x = i
                    break
    return x


def main(h):
    # start at a random place
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x


if __name__ == '__main__':
    x0, x = main(h)
    print(x0, x)
    print(h)
    assert h[x] > h[x0]

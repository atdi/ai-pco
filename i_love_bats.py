import random


def main():
    favourites = ['dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'bats', 'cats']  # change this
    print("I love " + random.choice(favourites))


if __name__ == '__main__':
    main()
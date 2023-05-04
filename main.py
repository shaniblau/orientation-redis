from extract import extract
from load import load


def main():
    files = extract("../dogs")
    load("../dogs", files)


if __name__ == '__main__':
    main()


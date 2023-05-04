from extract import extract
from load import load


def main():
    files = extract("/home/azureuser/dogs")
    load(files)


if __name__ == '__main__':
    main()


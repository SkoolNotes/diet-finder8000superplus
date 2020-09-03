import pandas

PATH = 'nndb_flat.csv'


def main():
    f = pandas.read_csv(PATH)
    print(f)

if __name__ == '__main__':
    main();


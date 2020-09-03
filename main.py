import csv

def main():
    with open(PATH, newline='') as csvf:
        reader = csv.reader(csvf, delimiter=' ', quotechar='"');
        for row in reader:
            print(', '.join(row))

if __name__ == '__main__':
    main();


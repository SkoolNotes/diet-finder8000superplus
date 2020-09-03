import pandas

DB_PATH = 'nndb_flat.csv' # 36 nutritional dimensions

DIET_SET = [1001, 6194, 35056] # salted butter, chicken broth, raw seal meat

def main():
    raw_data = pandas.read_csv(DB_PATH)
    filtered = raw_data[raw_data.ID.isin(DIET_SET)]
    print(filtered['ShortDescrip'])

if __name__ == '__main__':
    main();


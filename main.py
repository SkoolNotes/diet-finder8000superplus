import pandas as pd
import numpy  as np

DB_PATH = 'nndb_flat.csv' # 37 nutritional dimensions

DIET_SET = [1001, 6194, 35056] # salted butter, chicken broth, raw seal meat

def main():
    data = pd.read_csv(DB_PATH)
    data = data[data.ID.isin(DIET_SET)]
    data = data[data.columns[-37:]].to_numpy().transpose()
    print(data)

if __name__ == '__main__':
    main()


import pandas as pd
import numpy  as np

DB_PATH = 'nndb_flat.csv' # 37 nutritional dimensions

# DIET_SET = [1001, 6194, 35056] # salted butter, chicken broth, raw seal meat
# 790345

def main():
    data = pd.read_csv(DB_PATH)
    data = data[data.ID.isin(DIET_SET)]
    data = data[data.columns[-37:]].to_numpy().transpose()
    print(data)

def olve(nm, rdi):
    output = np.linalg.lstsq(names, nm, rdi)[0]
    for i in range(len(names)):
        print("You better freaking goddamn eat" + output[0][i][0] + "grams" + names[i])
    return output

    
    
if __name__ == '__main__':
    main()


import pandas as pd
import numpy  as np
from scipy.optimize import nnls
import pprint

weight = 60
# TODO: add back \/
# print("warning: pounds do not currently work")
# units = input("what units do you want to use? Type p for pounds and k for kilograms ")
# if units == "p":
#     weight = (int(input("what is your wieght in pounds? "))) * 2.20462262
# if units == "k":
#     weight = int(input("what is your weight in kilograms? "))

config = {
    'paths': {
        'subsample_result': 'data/sub_sample_result.csv',
        'food_nutrient': 'data/food_nutrient.csv',
        'food_name': 'data/food.csv'
    },
    'nutrients': [
        'Phenylalanine',
        'Valine'       ,
        'Leucine'      ,
        'Isoleucine'   ,
        'Lysine'       ,
        'Threonine'    ,
        'Tryptophan'   ,
        'Methionine'   ,
        'Histidine'    ,
        'Riboflavin'   , # vitamain b2
        'Phylloquinone', # vitamain K
        # 'Protein'      ,
    ],
    'target': [ # in miligrams
        33  * weight,
        24  * weight,
        43  * weight,
        19  * weight,
        38  * weight,
        20  * weight,
        5   * weight,
        19  * weight,
        14  * weight,

        # 0# 0.8 *weight # TODO: PROTIEN WEIGHT, PUT BACK, BELOW IS PLACEHOLDER
    ],
    'foods': [
        # 320146, # 2% milk
        # 334332, # sweet and sour pork chinese resturaunt
        327194, # cantaloupe amino acids
        327043, # kiwi
        # 325937, # turkey breakfast saucage (mild)
        326457, # carrots whole unprepared
        321692, # broccoli
        327388, # pass 2 oranges
        326690, # mustard
    ],

    'foodnames': [
        # '2% melk',
        # 'sweet sour pork',
        'cantaloupe',
        'kiwi',
        # 'turkey saucage',
        'carrots, whole, unprepared',
        'broccoli',
        'pass 2 oranges',
        'mustard'
    ]
}

def read_data():
    return {
        'subsample_result': pd.read_csv(config['paths']['subsample_result'],
            dtype={ 'nutrient_name': 'string' }),
        'food_nutrient':    pd.read_csv(config['paths']['food_nutrient'],
            low_memory=False).iloc[:, :4],
        'food_name':        pd.read_csv(config['paths']['food_name'])
    }

def olve(names, nm, rdi):
    # output = np.linalg.lstsq(nm, rdi, rcond=None)[0]
    output = nnls(nm, rdi)[0]
    print(nm.dot(output))
    for i,n in enumerate(names):
        print(f"You better goddamn eat {output[i]/10:.6f}g o'", n)
    return output

def main():
    csvs = read_data()
    legit_ids = set()
    food_by_id = np.zeros((len(config['nutrients']), len(config['foods'])))
    for ni, nutrient in enumerate(config['nutrients']):
        insts = csvs['subsample_result'][csvs['subsample_result']['nutrient_name'] == nutrient]
        insts = insts[insts.columns[0]]
        for nid in insts:
            amount = csvs['food_nutrient'][csvs['food_nutrient']['id'] == nid]
            legit_ids.add(int(amount['fdc_id']))
            try:
                ind = config['foods'].index(int(amount['fdc_id']))
                food_by_id[ni, ind] = float(amount['amount'])
            except ValueError:
                continue

    print(food_by_id)
    olve(config['foodnames'], food_by_id, config['target'])

    # for fid in legit_ids:
    #     name = csvs['food_name'][csvs['food_name']['fdc_id'] == fid]['description'].squeeze()
    #     print(fid, name)

if __name__ == '__main__':
    main()

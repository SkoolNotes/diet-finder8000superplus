import pandas as pd
import numpy  as np
import pprint

import rdi

config = {
    'paths': {
        'subsample_result': 'data/sub_sample_result.csv',
        'food_nutrient': 'data/food_nutrient.csv',
        'food_name': 'data/food.csv'
    },
    'rdi': {
        'Phenylalanine': 33,
        'Valine': 24,
        'Leucine': 43,
        'Isoleucine': 19,
        'Lysine': 38,
        'Threonine': 20,
        'Tryptophan': 5,
        'Methionine': 19,
        'Histidine': 14,
        'Protein': 0.8
    }
}

# 790345

def main():
    csvs = {
        'subsample_result': pd.read_csv(config['paths']['subsample_result'], dtype={ 'nutrient_name': 'string' }),
        # 'food_nutrient':    pd.read_csv(config['paths']['food_nutrient'], dtype={ 'id': int, 'fdc_id': int, 'nutrient_id': int, 'amount': float, 'data_points': int, 'derivation_id': int, 'min': float, 'max': float, 'median': float, 'footnote': 'string', 'min_year_acquired': int }),
        'food_nutrient':    pd.read_csv(config['paths']['food_nutrient'], low_memory=False),
        # 'food_name':        pd.read_csv(config['paths']['food_name'])
    }
    # by_nutrient_source = {}
    csvs['food_nutrient'] = csvs['food_nutrient'].iloc[:, :4]

    # print(csvs['food_nutrient'][csvs['food_nutrient']['id'] == 9638444])

    food = {}
    for nutrient in config['rdi']:
        insts = csvs['subsample_result'][csvs['subsample_result']['nutrient_name'] == nutrient]
        insts = insts[insts.columns[0]]
        for fid in insts:
            amount = csvs['food_nutrient'][csvs['food_nutrient']['id'] == fid]
            if (int(amount['fdc_id']) in food):
                food[int(amount['fdc_id'])][nutrient] = float(amount['amount'])
            else:
                food[int(amount['fdc_id'])] = {nutrient: float(amount['amount'])}
        # by_nutrient_source[nutrient] = insts

    # print(by_nutrient_source)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(food)
    # print(food)

    # print(csvs['food_nutrient'])


if __name__ == '__main__':
    main()


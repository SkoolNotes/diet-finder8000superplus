import pandas as pd
import numpy  as np
import pprint

print("warning: pounds do not currently work")
units = input("what units do you want to use? Type p for pounds and k for kilograms ")
weight = 0
if units == "p":
    #do unit conversion stuff
if units == "k"
    weight = input("what is your weight in kilograms? ")

config = {
    'paths': {
        'subsample_result': 'data/sub_sample_result.csv',
        'food_nutrient': 'data/food_nutrient.csv',
        'food_name': 'data/food.csv'
    },
    'rdi': {
        'Phenylalanine': 33*weight,
        'Valine': 24*weight,
        'Leucine': 43*weight,
        'Isoleucine': 19*weight,
        'Lysine': 38*weight,
        'Threonine': 20*weight,
        'Tryptophan': 5*weight,
        'Methionine': 19*weight,
        'Histidine': 14*weight,
        'Protein': 0.8*weight
    }
}

# 790345

def main():
    csvs = {
        'subsample_result': pd.read_csv(config['paths']['subsample_result'],
            dtype={ 'nutrient_name': 'string' }),
        'food_nutrient':    pd.read_csv(config['paths']['food_nutrient'], low_memory=False),
        # 'food_name':        pd.read_csv(config['paths']['food_name'])
    }
    csvs['food_nutrient'] = csvs['food_nutrient'].iloc[:, :4]

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

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(food)

def olve(nm, rdi):
    output = np.linalg.lstsq(names, nm, rdi)[0]
    for i in range(len(names)):
        print("You better freaking goddamn eat" + (output[0][i][0])*100 + "grams" + names[i])
    return output

    
    
if __name__ == '__main__':
    main()


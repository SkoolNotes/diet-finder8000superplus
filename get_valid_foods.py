import pandas as pd

nutrient = pd.read_csv('data/food_nutrient.csv', low_memory=False).iloc[:, 1]
descript = pd.read_csv('data/food.csv').iloc[:, 2]
for p in zip(nutrient, descript):
    print(*p)


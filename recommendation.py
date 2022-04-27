import pandas as pd
import numpy as np

data = pd.read_csv('static/data/data.csv')

menu_arr = data['food'].unique()
menu = menu_arr.tolist()

for i in range(len(menu)) :
    menu[i] = menu[i].title()

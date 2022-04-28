import pandas as pd

data = pd.read_csv('static/data/data.csv')

menu_arr = data['food'].unique()
menu = menu_arr.tolist()

for i in range(len(menu)) :
    menu[i] = menu[i].title()

def recommender(emotion):
    if emotion=='angry':
        food = 'Chocolate'
    elif emotion=='disgust':
        food = 'Watermelon Juice'
    elif emotion=='fear':
        food = 'Smoothies'
    elif emotion=='happy':
        food = 'Pizza'
    elif emotion=='neutral':
        food = 'Popcorn'
    elif emotion=='sad':
        food = 'Cake'
    elif emotion=='surprise':
        food = 'Pasta'
    return food

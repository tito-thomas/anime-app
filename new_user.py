import numpy as np
import pandas as pd
from joblib import dump, load
import random
def new_user(user_data):
    username = random.randint(0,1000000)
    experience = load("encoders/experience.pkl").transform(["Veteran"])[0]
    gender = load("encoders/gender.pkl").transform(["Male"])[0]
    generation = load("encoders/generation.pkl").transform(["Millenials"])[0]
    fav_anime_period = load("encoders/fav_anime_period.pkl").transform(["Classic"])[0]
    fav_genres = ["Shounen","Comedy","Romance"]

    #Vectorise genres
    
    descriptive_cols = pd.DataFrame({"username":[username], "experience":[experience], "gender":[gender],"generation":[generation], "fav_anime_period":[fav_anime_period]})
    columns = ['username','Shounen', 'Seinen', 'Mystery', 'Kids', 'Parody', 'Josei', 'Shoujo', 'Fantasy', 'Sports', 'School', 'Action', 'Drama', 'Supernatural', 'Ecchi', 'Martial Arts', 'Horror', 'Sci-Fi', 'Adventure', 'Game', 'Cars', 'Romance', 'Police', 'Super Power', 'Space', 'Music', 'Military', 'Historical', 'Harem', 'Psychological', 'Samurai', 'Magic', 'Thriller', 'Slice of Life', 'Mecha', 'Vampire', 'Shounen Ai', 'Comedy']
    genres = pd.DataFrame(columns=columns)
    #p = {genre: 0 for genre in columns}
    genres = pd.DataFrame(columns=columns)
    genres.loc["test"]=0
    genres["username"]=username
    row = [0]*len(columns)
    row.insert(0, username)

    for y in fav_genres:
        #encode each of the three favourite genres with value: 1
        genres[y] = 1

    v = pd.merge(descriptive_cols, genres)
    return v, user_data

sample_data = []
#print(new_user())
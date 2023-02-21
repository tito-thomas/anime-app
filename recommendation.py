import numpy as np
import pandas as pd
import sys

users = pd.read_csv(r"D:\dataset\users_cleaned.csv")
anime_lists = pd.read_csv(r"D:\dataset\animelists_cleaned.csv")

users.head()

#uf["birth_date"] = datetime.now() - uf["birth_date"]
#def date_to_age(days):
#    seconds = days.total_seconds()
#    years = seconds/3600/24/365.25
#    return int(years)

#age = uf["birth_date"].apply(to_age)

##ONE-HOT ENCODE GENRES

# Encode the genre field as a list of genres and one-hot encode it
#genre_encoded = df['genre'].str.split(', ')
#genre_encoded = genre_encoded.apply(lambda x: pd.Series(x))
#genre_encoded = pd.get_dummies(genre_encoded.stack()).sum(level=0)
#genre_df = pd.concat([df['anime_id'], genre_encoded], axis=1)
#df = pd.merge(df, genre_df, on='anime_id')


#LABEL ENCODING OF OTHER CATEGORIES
#creates dictionary for you
#from sklearn.preprocessing import LabelEncoder
#encoder = LabelEncoder()
#df['type_encoded'] = encoder.fit_transform(df['type'])
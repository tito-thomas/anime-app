import numpy as np
import pandas as pd
import sys

users = pd.read_csv(r"D:\dataset\users_cleaned.csv")
anime_lists = pd.read_csv(r"D:\dataset\animelists_cleaned.csv")

users.head()

#GET FAVOURITE GENRES FOR A SINGLE USER

#def single_user():     
# 
#     karthiga = ['Comedy', 'Shounen', 'Action']
#     Damonashu = ['Drama', 'Action', 'Sci-Fi']
#     bskai = ['Comedy', 'Romance', 'School']                                                        
#    #Example user/ must make work for all users
#    user = "bskai"
#    user_ratings = merge_rf.loc[merge_rf["username"]==user]
#    user_genres = []
    #Creating a list all genres in the top 10 for each user (including duplicates)
#    fav_list = [] #list of most popular genres for each user
#    for i in user_ratings["genre"]:
#            x = i.split()
#            user_genres = user_genres + x

#    final_result = []
#    for i,v in enumerate(user_genres):
#        if v!="nan":
#            new = v.replace(" ", "")
#            new = v.replace(",", "")
#            user_genres[i]=new
            

    #Find top 3 favourite most frequent genres in the top 10
#    for i in range(0, 3):
#        user_favs = []
#        most_popular = max(set(user_genres), key=user_genres.count)
#        user_favs.append(most_popular)
        #Remove genre from the list once added to favourites
#        for i in range(0, user_genres.count(most_popular)):
#            user_genres.remove(most_popular)

#        fav_list.append(user_favs)


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
#df['rating_encoded'] = encoder.fit_transform(df['rating'])
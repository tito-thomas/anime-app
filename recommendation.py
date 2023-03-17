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

#ATTEMPT AT FASTER EVALUATION

#test_arrays
#ef fast_evaluation():
    #Find nearest neighbours to test users in trainset 
    #index_neighbours = neighbours(test_arrays)
    #percentage_scores = []
    #print(len(index_neighbours))
    #print(test_arrays)
    #for index, i in enumerate(index_neighbours):
    #    test_arrays_index =test_arrays(index)
    #    print(test_arrays_index)
        #username = x.inverse_transform([i[0]])[0]
        #print(username)
    #    nframe = sim_frame([i])
        #print(nframe)
        #username = list(nframe["username"])
        #print(username[index])
    #    user_recommendations = recommendations(nframe, "TV")
        #print(username, user_recommendations)

        #rt = real_ratings.loc[real_ratings["username"]==username]
        #print(rt)
    #    score = 0
        #Check whether recommended shows are present in original ratings table
        #for show in user_recommendations:
        #    a_id = int(real_anime.loc[real_anime["title"]==show]["anime_id"])
            #u_ratings = real_ratings.loc[real_ratings["username"]==username]

        #    if int(a_id) in list(rt["anime_id"]): #if user watched the recommended show
        #        rating_row = real_ratings.loc[(real_ratings["username"]==username)&(real_ratings["anime_id"]==a_id)]
        #        score+=1
        #        if int(rating_row["my_score"])>=7:#user "likes" the show if they rated it higher than or equal to 7
        #            score+=1 #add an extra point if the user liked the shower

        #score = (score/10)*100 #max number of points is 10
        #percentage_scores.append(score)
        #if user liked show --> give double points
        #print(f"Score for user {username}: {score}%")

    #percentage_scores = np.array(percentage_scores)
    #average_score = np.average(percentage_scores)
    #print(f"Average recommendation score for Test users is {average_score}%")
    #return average_score

#fast_evaluation()
#include analysis of distance metric between neighbours e.g. cosine, euclidean 
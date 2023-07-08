import numpy as np
import pandas as pd
from joblib import dump, load
import random
import sys
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
import time
from time import perf_counter
import datatable as dt

preferences = sys.argv[1]
fav = sys.argv[2]

def new_user(preferences, fav_genres):
    user_vectors = pd.read_csv(r"D:\dataset\encoding\user_vectors.csv")
    preferences = preferences.split(" ")
    username, experience, gender, generation, fav_anime_period = preferences[0], preferences[1], preferences[2], preferences[3], preferences[4]

    #Encoding user features
    experience = load(r"C:\Final Project\anime-app\encoders\experience.pkl").transform([experience])[0]
    gender = load(r"C:\Final Project\anime-app\encoders\gender.pkl").transform([gender])[0]
    generation = load(r"C:\Final Project\anime-app\encoders\generation.pkl").transform([generation])[0]
    fav_anime_period = load(r"C:\Final Project\anime-app\encoders\fav_anime_period.pkl").transform([fav_anime_period])[0]
    
    fav_genres = fav_genres.split(',')#["Shounen","Comedy","Romance"]
    #fav_genres = fav_genres.split(' ')#console debugging
    #print(f"Fav_genres are {fav_genres} from C#")
    #Vectorise genres
    descriptive_cols = pd.DataFrame({"username":[username], "experience":[experience], "gender":[gender],"generation":[generation], "fav_anime_period":[fav_anime_period]})
    columns = ['Seinen','Fantasy','Cars','Magic','Shounen','Martial Arts','Mecha','Music','Thriller','Action','Josei','Sports','School','Ecchi','Drama',
               'Romance','Space','Shounen Ai','Parody','Shoujo Ai','Historical','Horror','Samurai','Slice of Life','Shoujo','Psychological','Dementia','Comedy','Police',
               'Adventure','Vampire','Sci-Fi','Harem','Demons','Kids','Supernatural','Super Power','Military','Mystery','Game']
    genres = pd.DataFrame(columns=columns)
    #print(len(columns))
    # p = {genre: 0 for genre in columns}
    genres.loc["test"]=0
    genres["username"]=username
    row = [0]*len(columns)
    row.insert(0, username)

    for y in fav_genres:
        #encode each of the three favourite genres with value: 1
        genres[y] = 1

    v = pd.merge(descriptive_cols, genres)

    #Re-encoding the username feature.
    encoder = LabelEncoder()
    #v = v.set_index("username")
    v.reset_index(drop=True, inplace=True)
    #print(v)
    user_vectors = pd.concat([user_vectors,v], ignore_index="True")
    #Drop username column so it doesnt affect k-neighbours
    user_vectors = user_vectors.drop("username",axis=1)

    #enc = encoder.fit_transform(user_vectors["username"])
    #print(f"{current_user}")
    #user_vectors["username"] = enc
    current_user = user_vectors.tail(1)
    #print(current_user)
    dump(encoder, r"C:\Final Project\anime-app\encoders\username.pkl")
    #print(user_vectors.iloc[241])
    return user_vectors, current_user

#print(new_user(preferences, fav)[1])
#py new_user.py "luffy Newbie Male Gen-Z Classic" "Action,Adventure,Shounen,Romance"

#function that returns a list of indexes of most similar users in "final_arrays" array
def neighbours(user, final_arrays):
    nc = NearestNeighbors(n_neighbors = 6, metric="cosine") #change to 6 and slice when done
    original = final_arrays
    final_arrays = final_arrays.values
    #print(final_arrays[241])
    train = nc.fit(final_arrays) 
    #print("fit worked")
    #print(user[0])
    n = train.kneighbors([user[0]], return_distance = False)

    n = [list(n[0][1:])]
    #print(n)
    #print(original.iloc[241])
    return n, final_arrays

#returns a dataframe of users that were in k-nearest neighbours list 
def sim_frame(neighbours, final_arrays):
    users = pd.read_csv(r"D:\dataset\encoding\user_frame.csv")
    sim_names = []
    #u = load(r"C:\Final Project\anime-app\encoders\username.pkl")

    for i in neighbours[0]: #loop through nested array
        #print(final_arrays[i][0])
        name = users.iloc[i]["username"]
        #print(name)
        #name = u.inverse_transform([final_arrays[i][0]]) #find usernames of similar users
        #print(final_arrays[i][2], name)
        sim_names.append(name)

    #build new dataframe of neighbours
    neighbour_frame = pd.DataFrame()
    for i in users.columns:
        neighbour_frame[i] = None

    for name in sim_names:
        user_row = users.loc[users["username"]==name]
        neighbour_frame = pd.concat([neighbour_frame, user_row])

    pd.options.display.max_rows = 999
    pd.set_option('display.max_columns', 500)
    return neighbour_frame

#Put anime that have most members at the top of each users "lists"
def get_anime(neighbours, media_type):
    #Get top rated TV shows or movies from each user
    ratings = pd.read_csv(r"D:\dataset\encoding\ratings_frame.csv")
    suggestions = [] #anime_id's of recommended anime
    for i in neighbours["username"]:
        user_ratings = ratings.loc[ratings["username"]==i]
        tv_shows = user_ratings[user_ratings["type"]=="TV"]
        movies = user_ratings[user_ratings["type"]=="Movie"]

        if media_type == "TV":
            show_ratings = tv_shows
        else:
            show_ratings = movies
        
        #There may be 0 movies in the user's top 10 list in which case we skip that user's recommendationan
        if len(show_ratings) > 1:
            top_rated = show_ratings.iloc[0]["anime_id"]#.encode("utf-8") #change to ids when creating the website to lookup the anime
            if top_rated not in suggestions:
                suggestions.append(top_rated)
            #print(top_rated)

    if len(suggestions)==0:
        print("No movies to recommend :/")
    
    return suggestions

#COLLABORATIVE FILTERING

def r_neighbours(anime, rating_vectors):
    #euclidean #find 2 most similar anime to each of the inital 5 recommendations
    nc = NearestNeighbors(n_neighbors = 3, metric="cosine") 
    train = nc.fit(rating_vectors.values) #fit the model with the ratings data
    n = train.kneighbors([anime], return_distance = False)
    return n

def r_neighbour_ids(initial):
    print("reading ratings")
    start = time.perf_counter()
    rating_vectors = pd.read_csv(r"D:\dataset\encoding\collab_scores.csv")
    #rating_vectors = dt.fread(r"D:\dataset\encoding\collab_scores.csv").to_pandas()
    one = time.perf_counter()
    print(f"Initial: {np.around((one-start),2)}s")

    print("done with ratings")
    n_ids = []
    for r in initial:
        a_vector = list(rating_vectors.loc[rating_vectors["anime_id"]==r].values)
        n_indexes = r_neighbours(a_vector[0], rating_vectors)[0]
        n_indexes = n_indexes[1:]
        for i in n_indexes:
            anime_id = rating_vectors.iloc[i]["anime_id"]
            n_ids.append(anime_id)
        
    two = time.perf_counter()
    print(f"Last: {np.around((two-one),2)}s")
    return n_ids

def get_additional_anime(initial):
    anime_frame = pd.read_csv(r"D:\dataset\encoding\anime_frame.csv")
    more_recs = pd.DataFrame()
    for i in r_neighbour_ids(initial):
        anime_row = anime_frame.loc[anime_frame["anime_id"]==i]
        more_recs = pd.concat([more_recs, anime_row])
        more_recs = more_recs.loc[:,["anime_id","title","studio", "genre","time_period", "fame"]]

    #exclude the first anime (the show being compared to)
    #more_recs=more_recs[1:]
    return list(more_recs["anime_id"])

#recommendations(neighbour_frame, "TV")
def get_recommendations(preferences, fav):
    start_time = time.perf_counter()
    results = new_user(preferences,fav)
    neighbour_ids = neighbours(np.array(results[1]), results[0])
    #print(neighbour_ids)
    neighbour_frame = sim_frame(neighbour_ids[0], neighbour_ids[1])
    suggestions = get_anime(neighbour_frame, "TV")

    one = time.perf_counter()
    #print(f"Initial: {np.around((one-start_time),2)}s")

    more_anime = get_additional_anime(suggestions)
    two = time.perf_counter()
    #print(f"Additional: {np.around((two-one),2)}s")

    end_time = time.perf_counter()
    #print(f"Total: {np.around((end_time-start_time),2)}s")
    return suggestions + more_anime
 

print(get_recommendations(preferences, fav))
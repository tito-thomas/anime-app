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
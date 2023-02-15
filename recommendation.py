import numpy as np
import pandas as pd
import sys

users = pd.read_csv(r"D:\dataset\users_cleaned.csv")
anime_lists = pd.read_csv(r"D:\dataset\animelists_cleaned.csv")

users.head()
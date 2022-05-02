import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/movie_dataset.csv")
# print(df.info())
# Helper functions
# Get the title of the movie from its index in dataframe
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]
# Get the index of the matched movie title
def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

# Content-based features
features = ['keywords','cast','genres','director']

# Fill all the null values in each feature with empty string to easily filter the data later
for feature in features:
	df[feature] = df[feature].fillna('')

def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print("Error:", row)


df["combined_features"] = df.apply(combine_features,axis=1)
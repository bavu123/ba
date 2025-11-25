import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
df = pd.read_csv("database.csv")
Vectorizer = TfidfVectorizer()
x = Vectorizer.fit_transform(df['question'])
model ={
    "vectorizer": Vectorizer,
    "X":"X",
    "answer" : df['answer'].tolist(),
    "question":df['question'].tolist()
}
pickle.dump(model,open("model.pkl","wb"))
print("model trained and saved succuessful")

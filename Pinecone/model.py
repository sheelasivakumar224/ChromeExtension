from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

import pinecone
api_key = "05be166d-0b87-4535-b875-ef117ddcadf7"
pinecone.init(api_key = api_key,environment="gcp-starter")


model = SentenceTransformer('all-MiniLM-L6-v2')


def embed(sentence):
    df = pd.DataFrame(columns = ['Text','Vector'])
    embeddings = model.encode(sentence)
    data = {'Text' : [sentence],'Vector':[embeddings.tolist()]}
    data_df = pd.DataFrame(data)
    df = pd.concat ([df,data_df])
    return df

# index = pinecone.Index('example')

# data = embed("S")
# result = index.upsert(vectors=zip(data.Text,data.Vector))

# print(result)
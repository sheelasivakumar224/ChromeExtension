from flask import Flask,render_template,request,redirect,url_for
import pinecone
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np


app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/embed',methods=["POST","GET"])
def home():
    text = request.form["sentence"]
    data = embed(text)
    index = pinecone.Index('example')
    result = index.upsert(vectors=zip(data.Text,data.Vector))
    return result

if __name__ == "__main__":
    app.run(debug=True)
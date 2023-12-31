from flask import Flask,render_template,request,redirect,url_for
import weaviate
import json


# Setting up an Api Key
auth_config = weaviate.AuthApiKey(api_key = "<API_KEY>")

# Creating an Instance of the Client
client = weaviate.Client(
    url = "<Cluster_URL>",
    auth_client_secret= auth_config,
        additional_headers={
        "X-HuggingFace-Api-Key":"<API_KEY>",
    }
)

app = Flask(__name__)

def addToClass(text):
    properties = {
        "prompt" : text
    }
    client.data_object.create(properties,class_name = "MyOwnPrompt")
    
def searchMyPrompt(text):
    res = client.query.get("MyOwnPrompt",['prompt']).with_near_text({
    "concepts": [text]
}).with_limit(3).do()
    prompts = res["data"]["Get"]["MyOwnPrompt"]
    prompt_texts = [prompt["prompt"] for prompt in prompts]
    results = []
    for text in prompt_texts:
        results.append(text)
    return results

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add',methods = ["POST","GET"])
def addPrompt():
    myPrompt = request.form['inputPrompt']
    addToClass(myPrompt)
    return redirect(url_for("index"))

@app.route('/search',methods=["POST","GET"])
def searchPrompt():
    search = request.form['searchPrompt']
    searchResult = searchMyPrompt(search)
    return render_template("index.html", texts = searchResult)

if __name__ == "__main__":
    app.run(debug=True)

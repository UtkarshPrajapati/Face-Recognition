from flask import Flask,request,jsonify,render_template,send_from_directory 
from flask_cors import CORS, cross_origin
import util
import pickle
import os 

persons = pickle.load(open("persons.pkl", "rb"))

app=Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
@cross_origin()
def index():
    return render_template("app.html",persons=persons)

@app.route("/classify_image",methods=["GET","POST"])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/about")
def contact_ui():
    return render_template("about.html")

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__=="__main__":
    print("Starting Python Flask Server For Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
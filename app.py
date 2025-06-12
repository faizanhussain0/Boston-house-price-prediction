from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([np.array(features)])
        return render_template("index.html", prediction_text="Predicted House Price: ${:.2f}".format(prediction[0]*1000))
    except:
        return render_template("index.html", prediction_text="Error: Please check input values.")

if __name__ == "__main__":
    app.run(debug=True)

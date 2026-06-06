from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

models, encoders, target_encoders = pickle.load(open("tourism_multi_prediction_model.pkl","rb"))

places = [
"Ajanta Caves","Ellora Caves","Daulatabad Fort",
"Shani Shingnapur","Trimbakeshwar Temple",
"Gateway of India","Raigad Fort",
"Sindhudurg Fort","Mahabaleshwar","Shirdi"
]

months = [
"January","February","March","April","May","June",
"July","August","September","October","November","December"
]

seasons = ["Winter","Summer","Monsoon","Post-Monsoon"]

weekends = ["Yes","No"]

@app.route("/", methods=["GET","POST"])
def index():

    result = None
    graph_data = None

    if request.method == "POST":

        place = request.form["place"]
        month = request.form["month"]
        season = request.form["season"]
        weekend = request.form["weekend"]

        data = pd.DataFrame([{
            "Place":place,
            "Month":month,
            "Season":season,
            "Weekend":weekend
        }])

        for col in encoders:
            data[col] = encoders[col].transform(data[col])

        results = {}

        for target in models:
            pred = models[target].predict(data)
            results[target] = target_encoders[target].inverse_transform(pred)[0]

        result = {
            "place": place,
            "crowd": results["Visitor_Count_Level"],
            "kids": results["Kids_Visitors"],
            "senior": results["Senior_Citizens"],
            "foreign": results["Foreign_Tourists"]
        }

        graph_data = [
            results["Visitor_Count_Level"],
            results["Kids_Visitors"],
            results["Senior_Citizens"],
            results["Foreign_Tourists"]
        ]

    return render_template(
        "index.html",
        places=places,
        months=months,
        seasons=seasons,
        weekends=weekends,
        result=result,
        graph_data=graph_data
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
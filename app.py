# TODO: fix animation bug + remove variable isAnimated
# TODO: fix zoom 

from flask import Flask, render_template, request
import csv 
import datetime
import os

app = Flask(__name__)

# load config
app.config.from_object("config.DevelopmentConfig")

# Create csv file for current day 
file_name = "csv/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".csv"
header = ["BON", "Destination", "No. of recipient", "Amount", "Date", "Time"]
if not os.path.exists(file_name):
    with open(file_name, "a") as file:
            writer = csv.writer(file)
            writer.writerow(header)


# Routes
@app.route("/", methods=["GET"])
def route_index():
    return render_template("index2.j2", size = app.config["SCANNER_BOX"])


@app.route("/bookings/", methods=["POST"])
def route_bookings():

    # check if fields exist 
    data = request.get_json()
    if "scanContent" not in data:
        return "Missing data for bons or destinations", 400

    data = data["scanContent"]
    if "bons" not in data or "destination" not in data or "recipients" not in data or "amounts" not in data:
        print(data)
        return "Missing data for bons or destinations", 400 

    # fetch data from request
    bons = data["bons"]
    recipients = data["recipients"]
    amounts = data["amounts"]
    destination = data["destination"]

    dt = datetime.datetime.now()
    date = dt.strftime("%Y-%m-%d")
    time = dt.strftime("%H-%M-%S")


    # write to csv file
    with open(file_name, "a") as file:
        for i in range(len(bons)):
            bon = bons[i]
            recipient = recipients[i]
            amount = amounts[i]
            row = [bon, destination, recipient, amount, date, time]
            writer = csv.writer(file)
            writer.writerow(row)

    return "OK", 200




# run the server (only development!)
if __name__ == "__main__":
    app.run(
        host = app.config["HOST"],
        port = app.config["PORT"],
        debug = app.config["DEBUG"],
        ssl_context = "adhoc"
        )
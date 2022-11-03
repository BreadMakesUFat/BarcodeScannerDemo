# TODO: improve design
# TODO: proper error handling + messages
# TODO: improve code structure 
# TODO: github?
# TODO: browser settings to directly access page (add exceptions)
# TODO: add updater for git?

from flask import Flask, render_template, request
import csv 
import datetime
import os

app = Flask(__name__)

# load config
app.config.from_object("config.DevelopmentConfig")

# Create csv file for current day 
file_name = "csv/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".csv"
header = ["BON", "Destination", "Date", "Time"]
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
    if "bon" not in data or "msg" not in data:
        print(data)
        return "Missing data for bon or msg", 400 

    # fetch data from request
    bon = data["bon"]
    msg = data["msg"]
    dt = datetime.datetime.now()
    date = dt.strftime("%Y-%m-%d")
    time = dt.strftime("%H-%M-%S")


    # write to csv file
    row = [bon, msg, date, time]
    with open(file_name, "a") as file:
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
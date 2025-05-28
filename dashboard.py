from flask import Flask, render_template, redirect
import json

app = Flask(__name__)

ALERT_FILE = "alerts.json"

@app.route("/")
def home():
    alerts = []
    try:
        with open(ALERT_FILE, "r") as f:
            alerts = [json.loads(line) for line in f if line.strip()]
    except FileNotFoundError:
        pass
    return render_template("dashboard.html", alerts=alerts)

#@app.route("/clear", methods=["POST"])
#def clear_alerts():
    #open(ALERT_FILE, "w").close()  # Vide le fichier
    #return redirect("/")

if __name__ =="__main__":
    app.run(debug=True, port=5000)
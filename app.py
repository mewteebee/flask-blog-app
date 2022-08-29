from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient("mongodb+srv://alexandermutebi:Alienware14@pocketbook.whuegz3.mongodb.net/test")
app.db = client.PocketBook

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    print([e for e in app.db.entries.find({})])
    if request.method == "POST":
        entry_content = request.form.get("content")
        date_of_entry = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, date_of_entry))
        app.db.entries.insert_one({"content": entry_content, "date": date_of_entry})

    entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]
    return render_template("index.html", entries=entries_with_date)
    
if __name__ == "__main__":
    app.run()


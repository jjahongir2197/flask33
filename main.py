from flask import Flask, render_template
from flask import redirect

app = Flask(__name__)

likes = 0

@app.route("/")
def home():

    return render_template(
        "index.html",
        likes=likes
    )

@app.route("/like")
def like():

    global likes

    likes += 1

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

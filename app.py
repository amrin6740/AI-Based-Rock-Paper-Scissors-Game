from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ["Rock", "Paper", "Scissors"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():

    user = request.form["choice"]

    computer = random.choice(choices)

    if user == computer:
        result = "🤝 It's a Tie!"

    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        result = "🎉 You Win!"

    else:
        result = "🤖 Computer Wins!"

    return render_template(
        "index.html",
        user=user,
        computer=computer,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
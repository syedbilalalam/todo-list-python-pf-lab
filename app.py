from flask import Flask, render_template, request, redirect, url_for, session

# Flask initialization code
app = Flask(__name__)
app.secret_key = "P-TODO-APP"

# Route for / as home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add/todo", methods=["POST"])
def add_todo():
    # request.form["cell"]
    # session["board"] = [""] * 9
    # session["turn"] = "X"
    # session["mode"] = mode
    return redirect(url_for("/"))

# @app.route("/play", methods=["GET", "POST"])
# def play():
#     board = session.get("board")
#     turn = session.get("turn")
#     mode = session.get("mode")

#     winner, win_line = check_winner(board)

#     if request.method == "POST" and not winner:
#         index = int(request.form["cell"])

#         if board[index] == "":
#             board[index] = turn
#             winner, _ = check_winner(board)

#             if not winner:
#                 if mode == "ai":
#                     if turn == "X":
#                         turn = "O"
#                         if "" in board:
#                             ai = smart_ai_move(board)
#                             board[ai] = "O"
#                             winner, _ = check_winner(board)
#                             if not winner:
#                                 turn = "X"
#                 else:
#                     # MULTIPLAYER TURN SWITCH
#                     turn = "O" if turn == "X" else "X"

#             session["board"] = board
#             session["turn"] = turn

#     winner, win_line = check_winner(board)

#     return render_template(
#         "index.html",
#         board=board,
#         winner=winner,
#         win_line=win_line,
#         mode=mode
#     )

# @app.route("/reset")
# def reset():
#     return redirect(url_for("game", mode=session.get("mode")))

# The following command will start the backend in debug mode
# Debug mode se error dhond ne mea aasani hoti hy
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import time
import os

app = Flask(__name__)

board = [" " for _ in range(9)]

# ---------- GAME LOGIC ----------
def check_winner(b):
    win_states = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
    for i,j,k in win_states:
        if b[i] == b[j] == b[k] and b[i] != " ":
            return b[i]
    return None

def is_full(b):
    return " " not in b

# ---------- MINIMAX ----------
def minimax(b, is_max):
    winner = check_winner(b)
    if winner == "O": return 1
    if winner == "X": return -1
    if is_full(b): return 0

    if is_max:
        best = -100
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = 100
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best

# ---------- ALPHA-BETA ----------
def alpha_beta(b, alpha, beta, is_max):
    winner = check_winner(b)
    if winner == "O": return 1
    if winner == "X": return -1
    if is_full(b): return 0

    if is_max:
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                val = alpha_beta(b, alpha, beta, False)
                b[i] = " "
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
        return alpha
    else:
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                val = alpha_beta(b, alpha, beta, True)
                b[i] = " "
                beta = min(beta, val)
                if beta <= alpha:
                    break
        return beta

# ---------- BEST MOVE ----------
def best_move(method="minimax"):
    best_val = -100
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            if method == "minimax":
                val = minimax(board, False)
            else:
                val = alpha_beta(board, -100, 100, False)

            board[i] = " "

            if val > best_val:
                best_val = val
                move = i

    return move

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    global board
    data = request.json
    pos = data["pos"]
    method = data["method"]

    if board[pos] != " ":
        return jsonify({"board": board})

    # Player move
    board[pos] = "X"

    winner = check_winner(board)
    if winner or is_full(board):
        return jsonify({
            "board": board,
            "winner": winner if winner else "Draw"
        })

    # AI move
    start = time.time()
    ai_move = best_move(method)
    end = time.time()

    if ai_move != -1:
        board[ai_move] = "O"

    winner = check_winner(board)

    return jsonify({
        "board": board,
        "winner": winner if winner else ("Draw" if is_full(board) else None),
        "time": round(end - start, 5)
    })

@app.route("/reset")
def reset():
    global board
    board = [" "] * 9
    return jsonify({"board": board})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
 
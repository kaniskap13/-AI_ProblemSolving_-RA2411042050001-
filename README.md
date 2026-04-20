# 🎮 Interactive Game AI – Tic-Tac-Toe System

## 📌 Problem Description

This project implements an **interactive Tic-Tac-Toe game** with an AI opponent.
The system allows a user to play against the computer through a web-based graphical interface.

The AI is designed to always make the **optimal move**, ensuring it never loses.

---

## 🧠 Algorithms Used

### 1. Minimax Algorithm

* A decision-making algorithm used in game theory
* Explores all possible game states
* Chooses the move that maximizes the AI’s chances of winning
* Guarantees optimal gameplay

### 2. Alpha-Beta Pruning

* Optimization of the Minimax algorithm
* Eliminates unnecessary branches in the game tree
* Reduces computation time
* Produces the same optimal result as Minimax but faster

---

## ⚙️ Features

✔ Fully interactive web-based UI
✔ Click-based gameplay (user = X, AI = O)
✔ AI responds instantly
✔ Displays:

* 🎉 You Win
* 🤖 AI Wins
* 🤝 Draw

✔ Compares:

* Execution time of algorithms
* Efficiency (reduced computations)

---

## 🏗️ Project Structure

```
AI_ProblemSolving_<RegisterNumber>/
│── app.py
│── requirements.txt
│── templates/
│     └── index.html
│── static/
│     └── style.css
```

---

## ▶️ Execution Steps

### 🔹 Run Locally

1. Install dependencies:

```
pip install flask
```

2. Run the application:

```
python app.py
```

3. Open browser:

```
http://127.0.0.1:5000
```

---

### 🔹 Run Online (Render Deployment)

1. Push project to GitHub
2. Connect repository to Render
3. Use settings:

**Build Command:**

```
pip install -r requirements.txt
```

**Start Command:**

```
gunicorn app:app
```

4. Access live app via generated URL

---

## 📊 Sample Output

* User clicks a box → **X appears**
* AI responds → **O appears**
* Game continues until:

  * Player wins → 🎉 *You Win*
  * AI wins → 🤖 *AI Wins*
  * No moves left → 🤝 *Draw*

---

## 📈 Comparison of Algorithms

| Feature        | Minimax | Alpha-Beta Pruning |
| -------------- | ------- | ------------------ |
| Accuracy       | High    | High               |
| Speed          | Slower  | Faster             |
| Nodes Explored | More    | Fewer              |
| Efficiency     | Lower   | Higher             |

---

## 🌐 Live Demo

🔗 Deployed Link: *(Add your Render link here)*

---

## 👨‍💻 Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript

---

## 📌 Conclusion

This project demonstrates how **Artificial Intelligence techniques** like Minimax and Alpha-Beta Pruning can be applied to build an optimal decision-making system in games.

---

## 🙌 Author

**Name:** Kaniska Prakash
**Register Number:** RA2411042050001

---

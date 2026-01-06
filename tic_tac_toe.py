import tkinter as tk
from tkinter import messagebox

# ----- Setup main window -----
root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"

# ----- Create buttons grid -----
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    # Check rows, columns, diagonals
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def reset_board():
    global current_player
    for row in buttons:
        for btn in row:
            btn["text"] = ""
    current_player = "X"

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} Wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

# Create buttons and assign click function
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('Arial', 40), width=5, height=2,
                                  command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Reset button
reset_btn = tk.Button(root, text="Reset", font=('Arial', 20), command=reset_board)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Run the app
root.mainloop()

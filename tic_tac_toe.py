import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Check for winning
def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="Darkcyan")
            buttons[combo[1]].config(bg="Darkcyan")
            buttons[combo[2]].config(bg="Darkcyan")
            winner_name = player_names[current_player]
            messagebox.showinfo("Tic-Tac-Toe", f"Player {winner_name} wins, Congrats! ")
            label.config(text=f"Winner: {winner_name}", fg="black")
            root.quit()
    # Checking for a tie
    if all(button["text"] != "" for button in buttons) and not any(button["text"] == "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        label.config(text="It's a tie!", fg="black")
        root.quit()

# On clicking a button
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

# Who's turn
def toggle_player():
    global current_player
    current_player = "X" if current_player =="O" else "O"
    label.config(text=f"{player_names[current_player]}'s turn", fg="black")

def get_player_names():
    global player_names
    player1_name = simpledialog.askstring("Enter Player 1's Name", "Enter the name of Player 1:")
    player2_name = simpledialog.askstring("Enter Player 2's Name", "Enter the name of Player 2:")
    player_names = {"X": player1_name, "O": player2_name}
    # label.config(text=f"{player_names[current_player]}'s turn", fg="black")

root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(background="Darksalmon")

title_label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 20),width=19, bg="Lightgray", fg="black")
title_label.pack(pady=10)

buttons_frame = tk.Frame(root, bg="gray")
buttons_frame.pack(expand=True)

buttons = [tk.Button(buttons_frame, text="", font=("normal", 25), width=7, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player ="X"
winner = False
player_names = {}

# Ask for players' names
get_player_names()

# Check whose turn it is
label = tk.Label(root, text=f"{player_names[current_player]}'s turn", font=("normal", 16), width=10, bg="Lightgray", fg="black")
label.pack()

root.mainloop()


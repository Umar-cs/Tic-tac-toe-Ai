import tkinter as tk
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AI Tic-Tac-Toe")
        self.board = [""] * 9
        self.current_player = "X"
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Helvetica", 24), width=6, height=2,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.show_winner()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.make_ai_move()

    def make_ai_move(self):
        available_moves = [i for i, val in enumerate(self.board) if val == ""]
        if available_moves:
            ai_move = random.choice(available_moves)
            row, col = divmod(ai_move, 3)
            self.make_move(row, col)

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]]) and \
                    (self.board[condition[0]] != ""):
                return True
        return False

    def show_winner(self):
        winner = self.current_player
        if winner == "X":
            winner = "Player"
        else:
            winner = "AI"
        winner_label = tk.Label(self.window, text=f"{winner} wins!", font=("Helvetica", 16))
        winner_label.grid(row=3, columnspan=3)
        self.disable_buttons()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.start()

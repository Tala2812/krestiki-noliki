import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry('300x350')

# Установка цвета фона окна
window.configure(bg='#FFC0CB')  # Нежно-розовый цвет

current_player = "X"  # По умолчанию
buttons = []

# Счетчики побед
score_x = 0
score_o = 0

def choose_symbol():
    global current_player
    choice = messagebox.askquestion("Выбор символа", "Вы хотите играть крестиками? (Да - крестики, Нет - нолики)")
    current_player = "X" if choice == "yes" else "0"

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_draw():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return False
    return True

def on_click(row, col):
    global current_player, score_x, score_o

    if buttons[row][col]['text'] != '':
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        if current_player == "X":
            score_x += 1
        else:
            score_o += 1
        update_score()
        if score_x == 3 or score_o == 3:
            messagebox.showinfo("Битва окончена", f"Игрок {current_player} победил!")
            reset_match()
        else:
            messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
            reset_game()
        return

    if check_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()
        return

    current_player = "0" if current_player == "X" else "X"

def reset_game():
    global current_player
    choose_symbol()
    for row in buttons:
        for button in row:
            button['text'] = ""

def reset_match():
    global score_x, score_o
    score_x = 0
    score_o = 0
    update_score()
    reset_game()

def update_score():
    score_label.config(text=f"X: {score_x} | O: {score_o}")

choose_symbol()

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=('Arial', 20), width=5, height=2,
                        bg='#8A2BE2',  # Фиолетовый цвет кнопок
                        fg='white',   # Белый цвет текста на кнопках
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

reset_button = tk.Button(window, text="Сброс", font=('Arial', 14),
                         bg='#8A2BE2',  # Фиолетовый цвет кнопки сброса
                         fg='white',    # Белый цвет текста на кнопке сброса
                         command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

score_label = tk.Label(window, text=f"X: {score_x} | O: {score_o}", font=('Arial', 14), bg='#FFC0CB')
score_label.grid(row=4, column=0, columnspan=3)

window.mainloop()
import tkinter as tk
from tkinter import messagebox

# إعداد النافذة الرئيسية
root = tk.Tk()
root.title("Tic-Tac-Toe")

# المتغيرات الأساسية
current_player = "X"
winner = False

def check_winner():
    global winner
    # الاحتمالات الـ 8 للفوز
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # تلوين الأزرار الفائزة باللون الأخضر الواضح وتغيير لون النص لأبيض ليكون واضحاً
            for index in combo:
                buttons[index].config(bg="green", fg="white", activebackground="green")
            
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

# إنشاء شريط النصوص لعرض الدور الحالي
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3, pady=10)

# إنشاء الأزرار الـ 9 الخاصة باللعبة
buttons = [
    tk.Button(root, text="", font=("normal", 25, "bold"), width=6, height=2, command=lambda i=i: button_click(i))
    for i in range(9)
]

# توزيع الأزرار على شكل شبكة 3x3
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# تشغيل التطبيق
root.mainloop()
import tkinter as tk
import random

 # メッセージボックス
from tkinter import messagebox


 # ランダムな数字を生成
def generate_new_number():
    return random.randint(1, 100)


 # 判定関数
def check_guess():
    global attempts, highscore
    try:
        attempts += 1
        guess = int(entry.get())
        if guess < correct_number:
            result_label.config(text="もっと大きいです", fg="blue")
        elif guess > correct_number:
            result_label.config(text="もっと小さいです", fg="red")
        else:
            result_label.config(text=f"おめでとうございます！正解です！", fg="green")
            entry.config(state=tk.DISABLED)
            check_button.config(state=tk.DISABLED)
            restart_button.config(state=tk.NORMAL)
            if highscore is None or attempts < highscore:
                highscore = attempts
                highscore_label.config(text=f"ハイスコア：試行回数{attempts}回")
                newrecord_label.config(text="New Record!!!")


        attempts_label.config(text=f"試行回数{attempts}回")
    except ValueError:
        result_label.config(text="数字を入力してください！", fg="orange")


def restart():
    global attempts, correct_number
     # config関連
    entry.config(state=tk.NORMAL)
    check_button.config(state=tk.NORMAL)
    result_label.config(text="")
    restart_button.config(state=tk.DISABLED)
    attempts_label.config(text="現在の試行回数0回")
    newrecord_label.config(text="")
     # 数値、エントリーのリセット
    correct_number = generate_new_number()
    attempts = 0
    entry.delete(0, tk.END)


def show_messagebox():
    global highscore
    result = messagebox.askokcancel("確認","ハイスコアをリセットしてもよろしいですか？")
    if result:
        print("ハイスコアをリセットしました。")
        highscore_label.config(text="ハイスコア：未設定")
        highscore = 1000
    else:
        print("キャンセルしました。")


 # ウインドウ設定
root = tk.Tk()
root.title("数当てゲーム")
root.geometry("600x400")

 # 正解の数字を設定(globalで変更)
correct_number = generate_new_number()

 # 試行回数0スタート
attempts = 0

highscore = None

 # ウィジェットの配置
tk.Label(root, text="数当てゲーム（1~100の数字を予想）", font=("Arial", 22)).pack(pady=10)
entry = tk.Entry(root, font=("Arial"), width=8, justify="center")
entry.pack()

check_button = tk.Button(root, text="判定", font=("Arial"), width=8, command=check_guess)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack()

 # 新記録ラベル
newrecord_label = tk.Label(root, text="", font=("Arial", 18), fg="magenta")
newrecord_label.pack()

attempts_label = tk.Label(root, text="現在の試行回数0回", font=("Arial", 18))
attempts_label.pack()

restart_button = tk.Button(root, text="もう一度プレイする",font=("Arial"), command=restart)
restart_button.pack()
restart_button.config(state=tk.DISABLED)

highscore_label = tk.Label(root, text="ハイスコア：未設定",font=("Arial", 18), fg="purple")
highscore_label.pack()

 # ハイスコアのリセットボタン
score_reset_button = tk.Button(root, text="ハイスコアをリセット",font=("Arial"), fg="red", command=show_messagebox)
score_reset_button.pack()

 # Enterキーで判定ボタンを押す
root.bind("<Return>", lambda event : check_button.invoke())

 # メインループ
root.mainloop()

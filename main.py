import tkinter as tk

root = tk.Tk()
root.title("4-7-8 呼吸法")
root.geometry("320x220")

label = tk.Label(root, text="準備", font=("Arial", 22), fg="white")
label.pack(expand=True)

btn = tk.Button(root, text="開始", width=10)
btn.pack(pady=10)

# 狀態控制
is_running = False
after_id = None

PHASES = [
    ("inhale", "吸氣", 4, "#3A7AFE"),  # 藍色
    ("hold",   "憋氣", 7, "#7B4DFF"),  # 紫色
    ("exhale", "呼氣", 8, "#2ECC71"),  # 綠色
]

STOP_BG = "#000000"  # 黑色

def step(phase_idx, remaining):
    global after_id

    if not is_running:
        return

    phase_key, phase_text, _, color = PHASES[phase_idx]

    # 切換背景顏色
    root.configure(bg=color)
    label.configure(bg=color, text=f"{phase_text} {remaining}")

    if remaining <= 1:
        next_idx = (phase_idx + 1) % len(PHASES)
        _, _, next_duration, _ = PHASES[next_idx]
        after_id = root.after(1000, step, next_idx, next_duration)
    else:
        after_id = root.after(1000, step, phase_idx, remaining - 1)

def toggle():
    global is_running, after_id

    if is_running:
        # 停止
        is_running = False
        if after_id:
            root.after_cancel(after_id)
            after_id = None

        # 背景全部回到黑色
        root.configure(bg=STOP_BG)
        label.configure(bg=STOP_BG, text="已停止")
        btn.configure(
            text="開始",
            bg=STOP_BG,
            bd=0,
            relief="flat",
            highlightthickness=0,
            activebackground=STOP_BG,
            highlightbackground=STOP_BG
        )
    else:
        # 開始
        is_running = True
        btn.configure(text="停止")

        _, _, duration, _ = PHASES[0]
        step(0, duration)


btn.configure(command=toggle)

root.mainloop()

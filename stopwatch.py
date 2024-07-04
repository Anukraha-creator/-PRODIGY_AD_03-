import tkinter as tk
from tkinter import ttk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.time_label = ttk.Label(self.root, text="00:00:000", font=("Arial", 40))
        self.time_label.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = ttk.Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = ttk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update_timer()

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def pause(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False
        self.time_label.config(text="00:00:000")

    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(self.elapsed_time, 60)
            milliseconds = (self.elapsed_time * 1000) % 1000
            time_string = f"{int(minutes):02}:{int(seconds):02}:{int(milliseconds):03}"
            self.time_label.config(text=time_string)
        self.root.after(10, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

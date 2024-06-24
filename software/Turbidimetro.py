import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DAQGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DAQ System")
        self.geometry("1800x1000")
        self.configure(bg='#2E2E2E')

        self.create_widgets()

    def create_widgets(self):
        # Sidebar
        self.sidebar = tk.Frame(self, bg='#1E1E1E', width=200, height=1000)
        self.sidebar.pack(side='left', fill='y')

        icons = ['Export', 'Settings', 'Logs']
        for icon in icons:
            btn = tk.Button(self.sidebar, text=icon, fg='#FFFFFF', bg='#333333', font=('Arial', 14))
            btn.pack(pady=10, padx=20, fill='x')

        # Main Content
        self.main_content = tk.Frame(self, bg='#2E2E2E')
        self.main_content.pack(side='right', fill='both', expand=True)

        self.create_graphs(self.main_content)

        # Control Panel
        self.control_panel = tk.Frame(self.main_content, bg='#333333', height=50)
        self.control_panel.pack(side='bottom', fill='x')

        buttons = ['Start', 'Stop', 'Reset']
        for button in buttons:
            btn = tk.Button(self.control_panel, text=button, fg='#FFFFFF', bg='#555555', font=('Arial', 14))
            btn.pack(side='left', padx=20, pady=10)

    def create_graphs(self, parent):
        self.graph_frame = tk.Frame(parent, bg='#2E2E2E')
        self.graph_frame.pack(side='top', fill='both', expand=True)

        figure, ax = plt.subplots(3, 1, figsize=(16, 8), dpi=100)
        figure.patch.set_facecolor('#2E2E2E')

        for i in range(3):
            ax[i].plot([random.randint(0, 10) for _ in range(10)], color='white')
            ax[i].set_facecolor('#2E2E2E')
            ax[i].tick_params(axis='x', colors='white')
            ax[i].tick_params(axis='y', colors='white')
            ax[i].spines['bottom'].set_color('white')
            ax[i].spines['top'].set_color('white')
            ax[i].spines['right'].set_color('white')
            ax[i].spines['left'].set_color('white')

        self.canvas = FigureCanvasTkAgg(figure, self.graph_frame)
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

if __name__ == "__main__":
    app = DAQGUI()
    app.mainloop()

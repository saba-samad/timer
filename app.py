import tkinter as tk
from tkinter import ttk
from datetime import datetime

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("400x600")  # Increased height for alarm settings
        self.root.configure(bg="#2C3E50")
        
        # Variables
        self.time_left = tk.StringVar()
        self.is_running = False
        self.end_time = None
        self.alarm_sound = None
        self.alarm_enabled = tk.BooleanVar(value=True)
        
        # Initialize pygame for sound
        import pygame
        pygame.mixer.init()
        self.alarm_sound = pygame.mixer.Sound("alarm.wav")  # You'll need to add an alarm.wav file
        
        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#2C3E50", pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Countdown Timer",
            font=("Helvetica", 24, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        title_label.pack(pady=20)
        
        # Existing time input frame code...
        
        # Add Alarm Settings frame
        alarm_frame = tk.Frame(main_frame, bg="#2C3E50")
        alarm_frame.pack(pady=10)
        
        # Alarm toggle
        self.alarm_checkbox = ttk.Checkbutton(
            alarm_frame,
            text="Enable Alarm Sound",
            variable=self.alarm_enabled,
            style="Custom.TCheckbutton"
        )
        self.alarm_checkbox.pack(pady=5)
        
        # Style for checkbox
        style = ttk.Style()
        style.configure("Custom.TCheckbutton",
                       background="#2C3E50",
                       foreground="#ECF0F1",
                       font=("Helvetica", 10))

    def update_timer(self):
        if self.is_running:
            remaining = self.end_time - datetime.now()
            
            if remaining.total_seconds() <= 0:
                self.time_left.set("Time's up!")
                self.is_running = False
                if self.alarm_enabled.get():
                    self.play_alarm()
            else:
                hours = int(remaining.total_seconds() // 3600)
                minutes = int((remaining.total_seconds() % 3600) // 60)
                seconds = int(remaining.total_seconds() % 60)
                
                self.time_left.set(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
                self.root.after(1000, self.update_timer)
    
    def play_alarm(self):
        if self.alarm_sound and self.alarm_enabled.get():
            self.alarm_sound.play()
            # Create a flash effect
            self.flash_screen()
    
    def flash_screen(self):
        current_bg = self.display_label.cget("background")
        if current_bg == "#2C3E50":
            self.display_label.configure(background="#E74C3C")
        else:
            self.display_label.configure(background="#2C3E50")
        
        if self.time_left.get() == "Time's up!" and self.alarm_enabled.get():
            self.root.after(500, self.flash_screen)
    
    def stop_timer(self):
        self.is_running = False
        if self.alarm_sound:
            self.alarm_sound.stop()
        self.display_label.configure(background="#2C3E50")
    
    def reset_timer(self):
        self.is_running = False
        if self.alarm_sound:
            self.alarm_sound.stop()
        self.hours.set("00")
        self.minutes.set("00")
        self.seconds.set("00")
        self.time_left.set("00:00:00")
        self.display_label.configure(background="#2C3E50")

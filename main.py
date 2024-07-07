import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
import os
import hashlib
import requests
import pygame
from themes import create_themes, apply_theme, update_text_widget_theme

# Initialize pygame mixer
pygame.mixer.init()

def generate_output_filename(text):
    """Generate a unique output filename based on the text input."""
    text_hash = hashlib.md5(text.lower().encode('utf-8')).hexdigest()
    return f"output/output_{text_hash}.mp3"

def is_online():
    """Check if the system is online by pinging a reliable website."""
    try:
        response = requests.get('http://www.google.com', timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def play_sound(file_path):
    """Play sound using pygame."""
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def speak_text():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    output_filename = generate_output_filename(text)

    if os.path.isfile(output_filename):
        play_sound(output_filename)
    else:
        if is_online():
            tts = gTTS(text=text, lang=language_var.get())
            tts.save(output_filename)
            play_sound(output_filename)
        else:
            messagebox.showwarning("Offline Error", "Text-to-speech conversion is not available offline.")

def save_audio():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    output_filename = generate_output_filename(text)

    if not os.path.exists('output'):
        os.makedirs('output')

    if os.path.isfile(output_filename):
        messagebox.showinfo("Save Audio", f"Audio already exists as {output_filename}\nFilename copied to clipboard")
    else:
        tts = gTTS(text=text, lang=language_var.get())
        tts.save(output_filename)
        messagebox.showinfo("Save Audio", f"Audio saved as {output_filename}\nFilename copied to clipboard")

    app.clipboard_clear()
    app.clipboard_append(output_filename)

app = tk.Tk()
app.title("Professional Text-to-Speech Application")
#app.iconbitmap('icon.ico')


if not os.path.exists('output'):
    os.makedirs('output')


# Create and apply themes
create_themes(app)

# Grid configuration
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)

# Text input
ttk.Label(app, text="Enter text:").grid(row=0, column=0, padx=10, pady=10, sticky="E")
text_entry = tk.Text(app, height=10, width=50, font=("Helvetica", 12), wrap="word")
text_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky="WE")

# Language selection
ttk.Label(app, text="Select language:").grid(row=1, column=0, padx=10, pady=10, sticky="E")
language_var = tk.StringVar(value="en")
language_options = ttk.Combobox(app, textvariable=language_var, state="readonly")
language_options['values'] = ('en', 'es', 'fr', 'de')
language_options.grid(row=1, column=1, padx=10, pady=10, sticky="W")

# Speech parameters
ttk.Label(app, text="Rate:").grid(row=2, column=0, padx=10, pady=10, sticky="E")
rate_var = tk.IntVar(value=150)
rate_slider = ttk.Scale(app, from_=50, to=300, orient=tk.HORIZONTAL, variable=rate_var)
rate_slider.grid(row=2, column=1, padx=10, pady=10, sticky="WE")

ttk.Label(app, text="Volume:").grid(row=3, column=0, padx=10, pady=10, sticky="E")
volume_var = tk.IntVar(value=100)
volume_slider = ttk.Scale(app, from_=0, to=100, orient=tk.HORIZONTAL, variable=volume_var)
volume_slider.grid(row=3, column=1, padx=10, pady=10, sticky="WE")

# Control buttons
speak_button = ttk.Button(app, text="Speak", command=speak_text)
speak_button.grid(row=4, column=0, padx=10, pady=10, sticky="E")

save_button = ttk.Button(app, text="Save Audio", command=save_audio)
save_button.grid(row=4, column=1, padx=10, pady=10, sticky="W")

# Theme selection
ttk.Label(app, text="Select Theme:").grid(row=5, column=0, padx=10, pady=10, sticky="E")
theme_var = tk.StringVar(value="Dark")
theme_options = ttk.Combobox(app, textvariable=theme_var, state="readonly")
theme_options['values'] = ('Light', 'Dark', 'Cyan', 'Yellow', 'Magenta')
theme_options.grid(row=5, column=1, padx=10, pady=10, sticky="W")
theme_options.bind("<<ComboboxSelected>>", lambda event: apply_theme(app, theme_var, text_entry, language_options, theme_options))

# Update text widget theme initially
update_text_widget_theme(theme_var, text_entry, language_options, theme_options)

# Apply the initial theme
apply_theme(app, theme_var, text_entry, language_options, theme_options)

app.mainloop()

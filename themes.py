import tkinter as tk
from tkinter import ttk

def create_themes(app):
    app.style = ttk.Style()
    app.style.theme_create("light", settings={
        ".": {
            "configure": {
                "background": "#FFFFFF",
                "foreground": "#000000",
                "font": ("Helvetica", 12)
            }
        },
        "TLabel": {
            "configure": {
                "background": "#FFFFFF",
                "foreground": "#000000"
            }
        },
        "TButton": {
            "configure": {
                "background": "#E0E0E0",
                "foreground": "#000000",
                "relief": "raised",
                "padding": 5
            }
        },
        "TCombobox": {
            "configure": {
                "background": "#FFFFFF",
                "foreground": "#000000"
            }
        }
    })

    app.style.theme_create("dark", settings={
        ".": {
            "configure": {
                "background": "#2E2E2E",
                "foreground": "#FFFFFF",
                "font": ("Helvetica", 12)
            }
        },
        "TLabel": {
            "configure": {
                "background": "#2E2E2E",
                "foreground": "#FFFFFF"
            }
        },
        "TButton": {
            "configure": {
                "background": "#5E5E5E",
                "foreground": "#FFFFFF",
                "relief": "raised",
                "padding": 5
            }
        },
        "TCombobox": {
            "configure": {
                "background": "#3E3E3E",
                "foreground": "#FFFFFF"
            }
        }
    })

    app.style.theme_create("cyan", settings={
        ".": {
            "configure": {
                "background": "#E0FFFF",
                "foreground": "#000000",
                "font": ("Helvetica", 12)
            }
        },
        "TLabel": {
            "configure": {
                "background": "#E0FFFF",
                "foreground": "#000000"
            }
        },
        "TButton": {
            "configure": {
                "background": "#B2DFEE",
                "foreground": "#000000",
                "relief": "raised",
                "padding": 5
            }
        },
        "TCombobox": {
            "configure": {
                "background": "#E0FFFF",
                "foreground": "#000000"
            }
        }
    })

    app.style.theme_create("yellow", settings={
        ".": {
            "configure": {
                "background": "#FFFFE0",
                "foreground": "#000000",
                "font": ("Helvetica", 12)
            }
        },
        "TLabel": {
            "configure": {
                "background": "#FFFFE0",
                "foreground": "#000000"
            }
        },
        "TButton": {
            "configure": {
                "background": "#FFFF99",
                "foreground": "#000000",
                "relief": "raised",
                "padding": 5
            }
        },
        "TCombobox": {
            "configure": {
                "background": "#FFFFE0",
                "foreground": "#000000"
            }
        }
    })

    app.style.theme_create("magenta", settings={
        ".": {
            "configure": {
                "background": "#FF00FF",
                "foreground": "#FFFFFF",
                "font": ("Helvetica", 12)
            }
        },
        "TLabel": {
            "configure": {
                "background": "#FF00FF",
                "foreground": "#FFFFFF"
            }
        },
        "TButton": {
            "configure": {
                "background": "#FF66FF",
                "foreground": "#FFFFFF",
                "relief": "raised",
                "padding": 5
            }
        },
        "TCombobox": {
            "configure": {
                "background": "#FF00FF",
                "foreground": "#FFFFFF"
            }
        }
    })

def apply_theme(app, theme_var, text_entry, language_options, theme_options):
    selected_theme = theme_var.get()
    if selected_theme == "Light":
        app.style.theme_use("light")
        app.config(bg="#FFFFFF")
        app.wm_title("Professional Text-to-Speech Application - Light Mode")
    elif selected_theme == "Dark":
        app.style.theme_use("dark")
        app.config(bg="#2E2E2E")
        app.wm_title("Professional Text-to-Speech Application - Dark Mode")
    elif selected_theme == "Cyan":
        app.style.theme_use("cyan")
        app.config(bg="#E0FFFF")
        app.wm_title("Professional Text-to-Speech Application - Cyan Mode")
    elif selected_theme == "Yellow":
        app.style.theme_use("yellow")
        app.config(bg="#FFFFE0")
        app.wm_title("Professional Text-to-Speech Application - Yellow Mode")
    elif selected_theme == "Magenta":
        app.style.theme_use("magenta")
        app.config(bg="#FF00FF")
        app.wm_title("Professional Text-to-Speech Application - Magenta Mode")

    update_text_widget_theme(theme_var, text_entry, language_options, theme_options)

def update_text_widget_theme(theme_var, text_entry, language_options, theme_options):
    selected_theme = theme_var.get()
    if selected_theme == "Light":
        text_entry.config(bg="#FFFFFF", fg="#000000")
        language_options.config(background="#FFFFFF", foreground="#000000")
        theme_options.config(background="#FFFFFF", foreground="#000000")
    elif selected_theme == "Dark":
        text_entry.config(bg="#2E2E2E", fg="#FFFFFF")
        language_options.config(background="#3E3E3E", foreground="#FFFFFF")
        theme_options.config(background="#3E3E3E", foreground="#FFFFFF")
    elif selected_theme == "Cyan":
        text_entry.config(bg="#E0FFFF", fg="#000000")
        language_options.config(background="#E0FFFF", foreground="#000000")
        theme_options.config(background="#E0FFFF", foreground="#000000")
    elif selected_theme == "Yellow":
        text_entry.config(bg="#FFFFE0", fg="#000000")
        language_options.config(background="#FFFFE0", foreground="#000000")
        theme_options.config(background="#FFFFE0", foreground="#000000")
    elif selected_theme == "Magenta":
        text_entry.config(bg="#FF00FF", fg="#FFFFFF")
        language_options.config(background="#FF00FF", foreground="#FFFFFF")
        theme_options.config(background="#FF00FF", foreground="#FFFFFF")

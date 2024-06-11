import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import pandas as pd
from PIL import Image, ImageTk, ImageSequence
import os
import ttkbootstrap as ttkb
from ttkbootstrap.constants import PRIMARY

class UtilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Utility App")
        self.root.geometry("800x600")  # Set the window size to 800x600
        self.root.resizable(False, False)  # Prevent resizing
        
        # Set the application icon
        icon_path = r'C:\Users\Info Agedis\Desktop\[APP]\[utility_app]\[1.0.1]\icona.ico'
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
        else:
            print(f"Icon file not found at {icon_path}")

        self.gif_label = self.create_gif_label(self.root)  # Initialize the GIF label once

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ttkb.Frame(self.root, padding="10 10 10 10")
        self.main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.frames = {}
        self.frames["home"] = self.create_home_frame()
        self.frames["format"] = self.create_generic_frame("Formatta file TXT", self.format_txt)
        self.frames["compare_duplicates"] = self.create_generic_frame("Confronta duplicati TXT", self.compare_duplicates)
        self.frames["compare_non_duplicates"] = self.create_generic_frame("Confronta non duplicati TXT", self.compare_non_duplicates)
        self.frames["compress"] = self.create_generic_frame("Comprimi immagini", self.compress_images)

        self.show_frame("home")

    def create_home_frame(self):
        frame = ttkb.Frame(self.main_frame)
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        button_specs = [
            ("Formatta file TXT", self.show_format_frame),
            ("Confronta duplicati TXT", self.show_compare_duplicates_frame),
            ("Confronta non duplicati TXT", self.show_compare_non_duplicates_frame),
            ("Comprimi immagini", self.show_compress_frame)
        ]

        for i, (text, command) in enumerate(button_specs):
            button = ttkb.Button(frame, text=text, bootstyle=PRIMARY, command=command)
            button.grid(column=0, row=i, padx=5, pady=5, sticky=(tk.W, tk.E))

        self.gif_label.grid(column=0, row=len(button_specs), padx=5, pady=5)  # Place the GIF label

        return frame

    def create_generic_frame(self, label_text, action_command):
        frame = ttkb.Frame(self.main_frame)
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        label = ttkb.Label(frame, text=label_text)
        label.grid(column=0, row=0, padx=5, pady=5)

        action_button = ttkb.Button(frame, text="Seleziona file", bootstyle=PRIMARY, command=action_command)
        action_button.grid(column=0, row=1, padx=5, pady=5)

        back_button = ttkb.Button(frame, text="Indietro", bootstyle=PRIMARY, command=self.show_home_frame)
        back_button.grid(column=0, row=2, padx=5, pady=5)

        self.gif_label.grid(column=0, row=3, padx=5, pady=5)  # Place the GIF label

        return frame

    def show_home_frame(self):
        self.show_frame("home")

    def show_format_frame(self):
        self.show_frame("format")

    def show_compare_duplicates_frame(self):
        self.show_frame("compare_duplicates")

    def show_compare_non_duplicates_frame(self):
        self.show_frame("compare_non_duplicates")

    def show_compress_frame(self):
        self.show_frame("compress")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def format_txt(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            separator = self.get_separator()
            if separator:
                self.format_file(file_path, separator)
    
    def format_file(self, file_path, separator):
        with open(file_path, 'r') as file:
            content = file.read()
        lines = content.splitlines()
        formatted_content = separator.join(lines)
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_path:
            with open(save_path, 'w') as file:
                file.write(formatted_content)
            messagebox.showinfo("Successo", "File formattato con successo.")
    
    def compare_duplicates(self):
        self.compare_files(duplicates=True)

    def compare_non_duplicates(self):
        self.compare_files(duplicates=False)

    def compare_files(self, duplicates):
        file1_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        file2_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file1_path and file2_path:
            separator = self.get_separator()
            if separator:
                list1 = pd.read_csv(file1_path, sep=separator, header=None)
                list2 = pd.read_csv(file2_path, sep=separator, header=None)
                if duplicates:
                    result = pd.merge(list1, list2, how='inner')
                else:
                    result = pd.concat([list1, list2]).drop_duplicates(keep=False)
                save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
                if save_path:
                    result.to_csv(save_path, sep=separator, index=False, header=False)
                    messagebox.showinfo("Successo", "Confronto completato con successo.")

    def get_separator(self):
        separator = simpledialog.askstring("Separatore", "Inserisci il separatore usato nel file:")
        return separator

    def compress_images(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.compress_images_in_folder(folder_path)
    
    def compress_images_in_folder(self, folder_path):
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(('png', 'jpg', 'jpeg')):
                    img_path = os.path.join(root, file)
                    self.compress_image(img_path)
        messagebox.showinfo("Successo", "Immagini compresse con successo.")
    
    def compress_image(self, img_path):
        img = Image.open(img_path)
        img = img.resize((600, 800), Image.LANCZOS)
        img = img.convert('RGB')
        img.save(img_path, "JPEG", dpi=(72, 72), quality=85)

    def create_gif_label(self, parent):
        self.gif_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(r'C:\Users\Info Agedis\Desktop\[APP]\[utility_app]\[1.0.1]\loading.gif'))]
        self.gif_index = 0
        label = ttkb.Label(parent)
        self.update_gif(label)
        return label

    def update_gif(self, label):
        frame = self.gif_frames[self.gif_index]
        self.gif_index = (self.gif_index + 1) % len(self.gif_frames)
        label.config(image=frame)
        self.root.after(125, self.update_gif, label)

if __name__ == "__main__":
    root = ttkb.Window(themename="superhero")
    app = UtilityApp(root)
    root.mainloop()

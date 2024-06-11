import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from PIL import Image, ImageTk, ImageSequence
import os
import requests
from io import BytesIO
import ttkbootstrap as ttkb
from ttkbootstrap.constants import PRIMARY

class UtilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Utility App")
        self.root.geometry("800x600")  # Set the window size to 800x600
        self.root.resizable(False, False)  # Prevent resizing
        self.root.iconbitmap(r'C:\Users\Info Agedis\Desktop\[APP]\icona.ico')  # Set the application icon

        self.create_widgets()

    def create_widgets(self):
        # Main frame to hold all other frames
        self.main_frame = ttkb.Frame(self.root, padding="10 10 10 10")
        self.main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure the root window to resize properly
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.frames = {}

        # Create individual frames for each functionality
        self.frames["home"] = self.create_home_frame()
        self.frames["format"] = self.create_format_frame()
        self.frames["compare_duplicates"] = self.create_compare_duplicates_frame()
        self.frames["compare_non_duplicates"] = self.create_compare_non_duplicates_frame()
        self.frames["compress"] = self.create_compress_frame()

        self.show_frame("home")

    def create_home_frame(self):
        frame = ttkb.Frame(self.main_frame)
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load the GIF and create a label to display it
        self.gif_label = self.create_gif_label(frame)
        self.gif_label.grid(column=0, row=4, padx=5, pady=5)

        # Button to navigate to the format file frame
        format_button = ttkb.Button(frame, text="Formatta file TXT", bootstyle=PRIMARY, command=self.show_format_frame)
        format_button.grid(column=0, row=0, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Button to navigate to the compare duplicates frame
        compare_duplicates_button = ttkb.Button(frame, text="Confronta duplicati TXT", bootstyle=PRIMARY, command=self.show_compare_duplicates_frame)
        compare_duplicates_button.grid(column=0, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Button to navigate to the compare non-duplicates frame
        compare_non_duplicates_button = ttkb.Button(frame, text="Confronta non duplicati TXT", bootstyle=PRIMARY, command=self.show_compare_non_duplicates_frame)
        compare_non_duplicates_button.grid(column=0, row=2, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Button to navigate to the compress images frame
        compress_images_button = ttkb.Button(frame, text="Comprimi immagini", bootstyle=PRIMARY, command=self.show_compress_frame)
        compress_images_button.grid(column=0, row=3, padx=5, pady=5, sticky=(tk.W, tk.E))

        return frame

    def create_format_frame(self):
        frame = ttkb.Frame(self.main_frame)
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load the GIF and create a label to display it
        self.gif_label = self.create_gif_label(frame)
        self.gif_label.grid(column=0, row=3, padx=5, pady=5)

        label = ttkb.Label(frame, text="Formatta file TXT")
        label.grid(column=0, row=0, padx=5, pady=5)

        select_file_button = ttkb.Button(frame, text="Seleziona file", bootstyle=PRIMARY, command=self.format_txt)
        select_file_button.grid(column=0, row=1, padx=5, pady=5)

        back_button = ttkb.Button(frame, text="Indietro", bootstyle=PRIMARY, command=self.show_home_frame)
        back_button.grid(column=0, row=2, padx=5, pady=5)

        return frame

    def create_compare_duplicates_frame(self):
        frame = ttkb.Frame(self.main_frame)
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load the GIF and create a label to display it
        self.gif_label = self.create_gif_label(frame)
        self.gif_label.grid(column=0, row=3, padx=5, pady=5)

        label = ttkb.Label(frame, text="Confronta duplicati TXT")
        label.grid(column=0, row=0, padx=5, pady=5)

        select_file_button = ttkb.Button(frame, text="Seleziona file", bootstyle=PRIMARY, command=self.compare_duplicates)
        select_file_button.grid(column=0, row=1, padx=5, pady=5)

        back_button = ttkb.Button(frame, text="Indietro", bootstyle=PRIMARY, command=self.show_home_frame)
        back_button.grid(column=0, row=2, padx=5, pady=5)

        return frame

    def create_compare_non_duplicates_frame(self):
        frame = ttkb.Frame(self.main_frame)
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load the GIF and create a label to display it
        self.gif_label = self.create_gif_label(frame)
        self.gif_label.grid(column=0, row=3, padx=5, pady=5)

        label = ttkb.Label(frame, text="Confronta non duplicati TXT")
        label.grid(column=0, row=0, padx=5, pady=5)

        select_file_button = ttkb.Button(frame, text="Seleziona file", bootstyle=PRIMARY, command=self.compare_non_duplicates)
        select_file_button.grid(column=0, row=1, padx=5, pady=5)

        back_button = ttkb.Button(frame, text="Indietro", bootstyle=PRIMARY, command=self.show_home_frame)
        back_button.grid(column=0, row=2, padx=5, pady=5)

        return frame

    def create_compress_frame(self):
        frame = ttkb.Frame(self.main_frame)
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load the GIF and create a label to display it
        self.gif_label = self.create_gif_label(frame)
        self.gif_label.grid(column=0, row=3, padx=5, pady=5)

        label = ttkb.Label(frame, text="Comprimi immagini")
        label.grid(column=0, row=0, padx=5, pady=5)

        select_folder_button = ttkb.Button(frame, text="Seleziona cartella", bootstyle=PRIMARY, command=self.compress_images)
        select_folder_button.grid(column=0, row=1, padx=5, pady=5)

        back_button = ttkb.Button(frame, text="Indietro", bootstyle=PRIMARY, command=self.show_home_frame)
        back_button.grid(column=0, row=2, padx=5, pady=5)

        return frame

    def show_home_frame(self):
        # Show the home frame
        self.show_frame("home")

    def show_format_frame(self):
        # Show the format frame
        self.show_frame("format")

    def show_compare_duplicates_frame(self):
        # Show the compare duplicates frame
        self.show_frame("compare_duplicates")

    def show_compare_non_duplicates_frame(self):
        # Show the compare non-duplicates frame
        self.show_frame("compare_non_duplicates")

    def show_compress_frame(self):
        # Show the compress images frame
        self.show_frame("compress")

    def show_frame(self, frame_name):
        # Bring the specified frame to the front
        frame = self.frames[frame_name]
        frame.tkraise()

    def format_txt(self):
        # Open a file dialog to select a text file to format
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            # Ask the user for the separator to use
            separator = self.get_separator()
            if separator:
                self.format_file(file_path, separator)
    
    def format_file(self, file_path, separator):
        # Read the content of the selected file
        with open(file_path, 'r') as file:
            content = file.read()
        # Split the content into lines and join them with the specified separator
        lines = content.splitlines()
        formatted_content = separator.join(lines)
        # Open a file dialog to select where to save the formatted file
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_path:
            # Write the formatted content to the new file
            with open(save_path, 'w') as file:
                file.write(formatted_content)
            messagebox.showinfo("Successo", "File formattato con successo.")
    
    def compare_duplicates(self):
        # Compare files to find duplicates
        self.compare_files(duplicates=True)

    def compare_non_duplicates(self):
        # Compare files to find non-duplicates
        self.compare_files(duplicates=False)

    def compare_files(self, duplicates):
        # Open file dialogs to select two text files for comparison
        file1_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        file2_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file1_path and file2_path:
            # Ask the user for the separator used in the files
            separator = self.get_separator()
            if separator:
                # Read the content of the files into dataframes
                list1 = pd.read_csv(file1_path, sep=separator, header=None)
                list2 = pd.read_csv(file2_path, sep=separator, header=None)
                if duplicates:
                    # Find the common rows (duplicates)
                    result = pd.merge(list1, list2, how='inner')
                else:
                    # Find the unique rows (non-duplicates)
                    result = pd.concat([list1, list2]).drop_duplicates(keep=False)
                # Open a file dialog to select where to save the result
                save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
                if save_path:
                    # Save the result to the new file
                    result.to_csv(save_path, sep=separator, index=False, header=False)
                    messagebox.showinfo("Successo", "Confronto completato con successo.")

    def get_separator(self):
        # Ask the user for the separator used in the files
        separator = tk.simpledialog.askstring("Separatore", "Inserisci il separatore usato nel file:")
        return separator

    def compress_images(self):
        # Open a file dialog to select a folder containing images
        folder_path = filedialog.askdirectory()
        if folder_path:
            # Compress the images in the selected folder
            self.compress_images_in_folder(folder_path)
    
    def compress_images_in_folder(self, folder_path):
        # Walk through the folder and compress each image file
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(('png', 'jpg', 'jpeg')):
                    img_path = os.path.join(root, file)
                    self.compress_image(img_path)
        messagebox.showinfo("Successo", "Immagini compresse con successo.")
    
    def compress_image(self, img_path):
        # Open the image file
        img = Image.open(img_path)
        # Resize the image
        img = img.resize((600, 800), Image.LANCZOS)
        # Convert the image to RGB format
        img = img.convert('RGB')
        # Save the image with reduced quality to compress it
        img.save(img_path, "JPEG", dpi=(72, 72), quality=85)

    def create_gif_label(self, parent):
        # Load the GIF
        self.gif_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(r'C:\Users\Info Agedis\Desktop\[APP]\loading.gif'))]
        self.gif_index = 0

        # Create a label to display the GIF
        label = ttkb.Label(parent)
        self.update_gif(label)
        return label


    def update_gif(self, label):
        frame = self.gif_frames[self.gif_index]
        self.gif_index = (self.gif_index + 1) % len(self.gif_frames)
        label.config(image=frame)
        self.root.after(125, self.update_gif, label)  # Change the delay as needed

if __name__ == "__main__":
    # Create the main application window with a specific theme
    root = ttkb.Window(themename="superhero")
    app = UtilityApp(root)
    root.mainloop()

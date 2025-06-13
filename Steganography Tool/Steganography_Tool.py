from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os

# ===== Steganography Functions =====
def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    binary_msg = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  
    pixels = list(img.getdata())

    new_pixels = []
    msg_index = 0

    for pixel in pixels:
        r, g, b = pixel[:3]
        if msg_index < len(binary_msg):
            r = (r & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            g = (g & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            b = (b & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)
    return output_path

def decode_image(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_data = ""
    for pixel in pixels:
        for color in pixel[:3]:
            binary_data += str(color & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""
    for byte in all_bytes:
        if byte == '11111110': 
            break
        message += chr(int(byte, 2))
    return message

# ===== GUI Actions =====
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png"), ("BMP Images", "*.bmp")])
    if file_path:
        image_path_entry.delete(0, END)
        image_path_entry.insert(0, file_path)

def encode_action():
    image_path = image_path_entry.get()
    secret_message = message_entry.get("1.0", END).strip()
    if not os.path.isfile(image_path):
        messagebox.showerror("Error", "Please select a valid image file.")
        return
    if not secret_message:
        messagebox.showwarning("Warning", "Secret message cannot be empty.")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    if output_path:
        try:
            encode_image(image_path, secret_message, output_path)
            messagebox.showinfo("Success", f"Message encoded and saved to:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed:\n{str(e)}")

def decode_action():
    image_path = image_path_entry.get()
    if not os.path.isfile(image_path):
        messagebox.showerror("Error", "Please select a valid image file.")
        return
    try:
        message = decode_image(image_path)
        messagebox.showinfo("Decoded Message", message)
    except Exception as e:
        messagebox.showerror("Error", f"Decoding failed:\n{str(e)}")

# ===== GUI Design =====
root = Tk()
root.title("🕵️‍♂️ Steganography Tool")
root.geometry("580x450")
root.configure(bg="#e9f5f9")

title_label = Label(root, text="🔐 Image Steganography Tool", font=("Helvetica", 16, "bold"), bg="#e9f5f9", fg="#2e7d7e")
title_label.pack(pady=15)

Label(root, text="Select Image:", font=("Helvetica", 12), bg="#e9f5f9", fg="#1e4b4b").pack()
frame = Frame(root, bg="#e9f5f9")
frame.pack()
image_path_entry = Entry(frame, width=50, font=("Helvetica", 10))
image_path_entry.pack(side=LEFT, padx=5, pady=10)
Button(frame, text="Browse", command=select_image, bg="#82caff", fg="black", font=("Helvetica", 10, "bold")).pack()

Label(root, text="Enter Secret Message:", font=("Helvetica", 12), bg="#e9f5f9", fg="#1e4b4b").pack()
message_entry = Text(root, height=5, width=60, font=("Helvetica", 10))
message_entry.pack(pady=(0, 15))

Button(root, text="🔏 Encode Message", command=encode_action, width=25, height=2,
       bg="#4CAF50", fg="white", font=("Helvetica", 11, "bold")).pack(pady=6)

Button(root, text="🕵️ Decode Message", command=decode_action, width=25, height=2,
       bg="#ff9800", fg="white", font=("Helvetica", 11, "bold")).pack(pady=6)

footer = Label(root, text="Made with Prashant in Python", font=("Helvetica", 9), bg="#e9f5f9", fg="#888")
footer.pack(side=BOTTOM, pady=10)
root.mainloop()
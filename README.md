# Steganography-Tool
A simple yet powerful Python-based GUI application that allows you to hide (encode) secret text messages inside images and retrieve (decode) them later all using steganography principles. Built with Tkinter for the GUI and PIL (Pillow) for image processing, this tool is perfect for anyone interested in cybersecurity, information hiding, or privacy.

# What is Steganography?
Steganography is the technique of hiding data within non-secret data. In this tool, your secret message is hidden inside an image file by modifying the least significant bits (LSBs) of its pixel values — in a way that’s invisible to the human eye.

# Features
1. Encode any secret message into a .png or .bmp image
2. Decode hidden messages from stego images
3. Simple and user-friendly graphical interface
4. Visual feedback for success or error messages
5. No internet required – works completely offline
6. End-to-end working example using Python

# How It Works
1. The tool changes your secret message (like "Hello") into binary code — a form that computers understand (like 01001000...).
2. It then hides this binary code inside the colors of the image (in the red, green, and blue parts of each pixel). It does this by changing the tiniest part (called the    Least Significant Bit or LSB) of each color — so small that the human eye can’t notice the change.
3. At the end of the hidden message, the tool adds a special code (1111111111111110) to show that the message is finished.
4. When decoding, the tool checks those tiny bits from the image again, finds your hidden message, and converts it back into normal readable text.

# Technologies Used
1. Python 3.x
2. Tkinter (built-in GUI library)
3. Pillow (Python Imaging Library)

# Installation
1. Make sure you have Python installed. If not, download it from: https://www.python.org/downloads/
2. Install Pillow (image handling library): pip  install pillow
3. Run the application: python  your_file_name.py

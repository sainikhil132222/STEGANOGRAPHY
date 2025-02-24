import cv2
import os
import base64

# Load the image
img = cv2.imread("mypic.jpg")  # Ensure this image exists in the same folder

if img is None:
    print("Error: Image not found! Check the file path.")
    exit()

# Get secret message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Convert the message to a base64 string to avoid ASCII issues
encoded_msg = base64.b64encode(msg.encode()).decode()

# Store the passcode with the encoded message
with open("passcode.txt", "w") as f:
    f.write(f"{password}|{encoded_msg}")  # Store as text

cv2.imwrite("encryptedImage.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  # Save as JPG with max quality
print("Message encrypted successfully! Image saved as 'encryptedImage.jpg'.")

# Open the image (for Windows)
os.system("start encryptedImage.jpg")

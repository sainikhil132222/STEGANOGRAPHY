import cv2
import base64

# Load the encrypted image
img = cv2.imread("encryptedImage.jpg")

if img is None:
    print("Error: Encrypted image not found! Run encryption first.")
    exit()

# Read the stored passcode and encoded message
try:
    with open("passcode.txt", "r") as f:
        stored_data = f.read().strip()
        stored_password, encoded_msg = stored_data.split("|")
except (FileNotFoundError, ValueError):
    print("Error: Passcode file missing or corrupted!")
    exit()

# Get the passcode from the user
password = input("Enter passcode for Decryption: ")

# Check if the passcode matches
if password != stored_password:
    print("YOU ARE NOT AUTHORIZED!")
    exit()

# Decode the message
decrypted_msg = base64.b64decode(encoded_msg.encode()).decode()

print("Decrypted message:", decrypted_msg)


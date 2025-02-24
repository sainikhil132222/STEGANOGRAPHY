# Steganography Photo Encrypting with Passcode

## Overview
This project implements **image steganography** to hide secret messages inside images using a passcode for additional security. The encryption and decryption processes ensure that data remains hidden and accessible only with the correct passcode. The project is built using **Python** and utilizes the **OpenCV (cv2) library** for image processing.

## Features
- Encrypts a secret message within an image.
- Passcode-protected decryption ensures security.
- Maintains image quality without noticeable alterations.
- Uses **OpenCV (cv2)** for efficient image handling.

## Technologies Used
- **Python**
- **OpenCV (cv2)**
- **NumPy**
- **PIL (Pillow)**

## Installation
Ensure you have Python installed on your system. Then, install the required libraries:

```sh
pip install opencv-python numpy pillow
```

## Usage

### Encryption (Hiding a Message)
1. Run the `encrypt.py` script.
2. Provide the input image, secret message, and passcode.
3. The output will be a new steganographic image with the hidden message.

```sh
python encrypt.py
```

### Decryption (Retrieving a Message)
1. Run the `decrypt.py` script.
2. Enter the steganographic image and the passcode.
3. The hidden message will be revealed if the passcode is correct.

```sh
python decrypt.py
```

## Example
### Encrypting a Message:
```
Enter image file: secret_image.png
Enter secret message: "Top secret info"
Enter passcode: 1234
Output image saved as: encoded_image.png
```

### Decrypting a Message:
```
Enter encoded image: encoded_image.png
Enter passcode: 1234
Decrypted message: "Top secret info"
```

## Future Enhancements
- Support for multiple image formats and higher resolutions.
- GUI-based implementation for easier use.
- Advanced encryption techniques for enhanced security.

## License
This project is open-source and free to use.

## Author
[ RAMOJU VARAHA NARASIMHA SAI NIKHIL ]

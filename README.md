**IMAGE ENCRYPTION**

Image Encryption/Decryption Tool (XOR-based)
This repository contains a Python script that implements a simple encryption and decryption tool for image files. The core of the tool uses the XOR (exclusive OR) operation with a user-defined key to modify the pixel values of the image. The XOR operation is symmetric, meaning the same key is used for both encryption and decryption.

Overview
The script provides functionality to encrypt or decrypt image files using the XOR operation on their pixel data. By applying this operation on the RGB values of each pixel, we can either encrypt an image (by altering its pixel values) or decrypt it (by applying the same operation with the same key to retrieve the original image).

Key Features:
Image Processing: Works with any image format supported by the Python Imaging Library (PIL), such as .png, .jpg, .bmp, etc.

Encryption and Decryption: XOR operation is used to encrypt and decrypt the image. The same operation and key are used for both actions, making the process reversible.

User-defined Key: Users can input a custom key (a number between 0 and 255) for the XOR operation.

Save to File: The processed image (either encrypted or decrypted) is saved to a specified location, with the option to choose a custom directory.

How it Works
The script opens the image using the Python Imaging Library (PIL), then applies the XOR operation to each pixel's RGB values using the provided key. For encryption, this will scramble the image data, while for decryption, it will return the image back to its original form if the same key is used.

Encryption: When the image is processed with a key, each pixel's red (R), green (G), and blue (B) values are XORed with the key, resulting in altered pixel colors.

Decryption: When the same key is applied again to the altered image, the XOR operation will reverse the changes and recover the original image.

Requirements
Python 3.x

PIL or Pillow library (Python Imaging Library)

You can install the required library using pip:

bash
Copy
pip install pillow
Usage Instructions
Clone or download the repository to your local machine.

Run the script image_encryption_tool.py using Python.

Example of Running the Script
When you run the script, it will prompt you for the following inputs:

bash
Copy
Enter image path: path_to_your_image.jpg
Enter output path or directory: path_to_save_encrypted_image/
Enter key (0-255): 123
Image path: Provide the full path to the image you wish to process.

Output path: Specify the directory where the processed image should be saved. If you provide a directory path, the tool will save the processed image in that directory with a new name.

Key: Enter an integer between 0 and 255. This key is used in the XOR operation to encrypt or decrypt the image. Ensure that the key remains the same when decrypting the image to get the original back.

Example of Encryption and Decryption:
Encryption: If you input an image and a key, it will encrypt the image and save it to the output path.

Decryption: You can then take the encrypted image, provide the same key, and the script will decrypt the image back to its original form.

Error Handling
FileNotFoundError: If the provided image file path is incorrect or the file doesn't exist.

Invalid Key: The key should be an integer between 0 and 255. Any other input will raise a validation error.

General Errors: Any other errors encountered during the image processing will be caught and displayed.

Code Explanation
process_image(): This function handles the core logic of opening the image, converting it to RGB, processing each pixel with the XOR operation, and saving the processed image.

It takes three arguments: image_path (input image), output_path (where the processed image will be saved), and key (integer used for XOR operation).

It uses the PIL.Image.open() method to open the image and img.load() to load pixel data.

For each pixel, it applies the XOR operation on the RGB values (r ^ key, g ^ key, b ^ key).

The processed image is then saved to the specified output path.

main(): This function handles user input and runs the image processing function. It prompts the user for input and calls process_image() with the appropriate parameters.

Error Handling: The script catches potential errors such as invalid file paths, incorrect keys, and other general exceptions.

Example Output
Upon successful processing, the script will print a confirmation message with the path to the processed image:

bash
Copy
Image processed successfully: path_to_output_directory/processed_image.jpg
License
This repository is licensed under the MIT License. See the LICENSE file for more details.

Contributions
Feel free to fork the repository and submit pull requests for improvements or bug fixes. Contributions are always welcome!

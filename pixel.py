from PIL import Image
import os

def process_image(image_path, output_path, key):
    """Encrypt or decrypt an image using XOR operation with the key"""
    try:
        # Open image and convert to RGB
        img = Image.open(image_path).convert('RGB')
        pixels = img.load()
        
        # Process each pixel
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)
        
        # If output_path is a directory, create new filename
        if os.path.isdir(output_path):
            original_name = os.path.basename(image_path)
            output_path = os.path.join(output_path, f"processed_{original_name}")
        
        img.save(output_path)
        print(f"Image processed successfully: {output_path}")
        
    except FileNotFoundError:
        print("Error: Image file not found")
    except Exception as e:
        print(f"Error processing image: {e}")

def main():
    print("Image Encryption/Decryption Tool")
    print("(Uses XOR operation with the same key for both operations)")
    
    try:
        # Get user inputs
        image_path = input("Enter image path: ").strip()
        output_path = input("Enter output path or directory: ").strip()
        key = int(input("Enter key (0-255): "))
        
        # Validate key
        if not 0 <= key <= 255:
            print("Key must be between 0 and 255")
            return
        
        process_image(image_path, output_path, key)
        
    except ValueError:
        print("Invalid key - must be a number between 0-255")
    except KeyboardInterrupt:
        print("\nOperation cancelled")

if __name__ == "__main__":
    main()

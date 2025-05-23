import os

def xor_cipher(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as f_in:
            data = f_in.read()
        
        encrypted_data = bytes([byte ^ key for byte in data])
        
        with open(output_file, 'wb') as f_out:
            f_out.write(encrypted_data)

        print(f"Encryption complete: '{input_file}' -> '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_path = "plain.txt"       
output_path = "encrypted.txt"  
xor_key = int(os.environ.get("XOR_KEY", "0"))                  

xor_cipher(input_path, output_path, xor_key)

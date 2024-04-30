import numpy as np
from PIL import Image

def encrypt_image(input_image_path, output_encrypted_path):
    img = Image.open(input_image_path)
    img_arr = np.array(img)

    key = np.random.randint(0, 256, size=img_arr.shape, dtype=np.uint8)

    encrypted_img_arr = np.bitwise_xor(img_arr, key)

    encrypted_img = Image.fromarray(encrypted_img_arr)
    encrypted_img.save(output_encrypted_path)
    np.save(output_encrypted_path, key)


def decrypt_image(input_encrypted_path, output_image_path, key):
    encrypted_img = Image.open(input_encrypted_path)
    encrypted_img_arr = np.array(encrypted_img)
    secret_key = np.load(key)

    decrypted_img_arr = np.bitwise_xor(encrypted_img_arr, secret_key)

    decrypted_img = Image.fromarray(decrypted_img_arr)
    decrypted_img.save(output_image_path)

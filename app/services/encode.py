import os
import io
from base64 import encodebytes
from PIL import Image

# finds dir of images then encodes it into b64 for file transfer with http
def get_encoded_image(image_name):
    image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images', image_name)    
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='JPEG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img
 
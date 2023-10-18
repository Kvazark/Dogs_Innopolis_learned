import requests
import numpy as np
import cv2
import matplotlib.pyplot as plt

files = {'image': ('image.jpg', open('bus.jpg', 'rb'))}

response = requests.post(
    'http://127.0.0.1:8000/image',
    files=files
)
print(response)




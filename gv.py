
"""Detects text in the file."""
from google.cloud import vision
import io
import os

# create the Google vision Api Service
# download the json file from the google cloud 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"user04102019-040e6651e330.json"

#Give the Path/ Location where the 
path = "C:/Users/mayank singh/Desktop/gvision/logo.jpg"

client = vision.ImageAnnotatorClient()


with io.open(path, 'rb') as image_file:
	content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
for text in texts:
	print(text.description)
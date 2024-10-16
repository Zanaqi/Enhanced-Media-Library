import os, io
import pandas as pd
from google.cloud import vision_v1 as vision
from google.cloud.vision_v1 import types


secret_file_name = r'enhanced-media-library-ff22693ff6d8.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f'secret/{secret_file_name}'
client = vision.ImageAnnotatorClient()

image_name = r'test-image-1.JPG'
image_path = f'images/test/{image_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response = client.label_detection(image=image)
labels = response.label_annotations

df = pd.DataFrame(columns=['description', 'score', 'topicality'])

for label in labels:
    df = pd.concat(
        [
            pd.DataFrame([[
                label.description, 
                label.score, 
                label.topicality
            ]], columns=df.columns), df
        ], ignore_index=True
    )

df = df.sort_values(by='score', ascending=False, ignore_index=True)

print(df)

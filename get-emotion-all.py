import os
import sys
import pathlib
from fer import FER
import matplotlib.pyplot as plt 

path=sys.argv[1]

img_files = [f for f in os.listdir(path) if f.endswith('.jpg')]

for imgfile in img_files:
	img = plt.imread(imgfile)
	detector = FER(mtcnn=True)
	emotion, score = detector.top_emotion(img)
	print(imgfile,emotion,score)

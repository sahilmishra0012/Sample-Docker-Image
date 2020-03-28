from flask import Flask, render_template, request,redirect
from cv2 import cv2
import sys
import os
import db_extraction

app = Flask(__name__,template_folder='')

app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['GET','POST'])
def capture():
    if request.method == 'POST':
        print(request.files['image'])
        image = request.files["image"]
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], 'IM12.jpg')) 
        path='/home/samkiller007/Downloads/Projects/Machine Learning/Automated Attendance System/Dataset/Images'
        embeddings=image_embedding.generate_image_encoding(path)
        k=db_extraction.get_student(embeddings)
        if k==('Not Found','Not Found'):
            return render_template('notfound.html')
        else:
            data={'name':k[1],'roll':k[0]}
            return render_template('found.html',data=data)
    return render_template('notfound.html')

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8080, debug=True)
from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename
import json
import numpy as np
import cv2
import pickle

from .conf_receive_rabbitmq import RabbitmqPublish

app = Flask(__name__)

conf_rabbitmq = RabbitmqPublish()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def receive_file():
    """API Rest responsible for receiving images sent by the user."""

    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/')

        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect('/')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # Construct an array from data in a text or binary file.
            numpy_image = np.fromfile(file, dtype=np.uint8, count=-1, sep="", offset=0)

            # convert numpy array to image
            # imdecode: Reads an image from a buffer in memory.
            # cv2.COLOR_BGR2RGB = 4 ( >0 Return a 3-channel color image.)
            image = cv2.imdecode(numpy_image, cv2.COLOR_BGR2RGB)

            # Python object (dict):
            data = {"image": image, "filename": file.filename, "width": 384, "height": 384}

            # serializing JSON:
            data_serialized = pickle.dumps(data, protocol=0)

            # Send to RabbitMQ's 'json_data' queue
            conf_rabbitmq.basic_publish(data_serialized)

            return redirect('/')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''